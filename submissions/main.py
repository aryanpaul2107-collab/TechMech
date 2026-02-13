"""
F1 Racing Challenge - Main Game File
A high-speed Formula 1 racing game built with Pygame
"""

import pygame
import sys
from config import *
from cars import PlayerCar, ObstacleCar
from game import Road, ParticleSystem, GameStateManager, GameState
from ui import HUD, MainMenu
from utils import CollisionDetector, SoundManager


class F1RacingGame:
    """Main game class that orchestrates all components"""
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Setup display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        # Game state management
        self.state_manager = GameStateManager()
        
        # Initialize game components
        self.road = Road()
        self.particles = ParticleSystem()
        self.hud = HUD()
        self.menu = MainMenu()
        self.sound_manager = SoundManager()
        self.collision_detector = CollisionDetector()
        
        # Player car
        road_left, road_right = self.road.get_boundaries()
        start_x = SCREEN_WIDTH // 2 - PLAYER_CAR_WIDTH // 2
        start_y = SCREEN_HEIGHT - PLAYER_CAR_HEIGHT - 20
        self.player = PlayerCar(start_x, start_y)
        
        # Obstacles
        self.obstacles = []
        
        # Game variables
        self.score = 0
        self.spawn_timer = 0
        self.spawn_delay = INITIAL_SPAWN_DELAY
        self.last_milestone = 0
        self.running = True
        
    def reset_game(self):
        """Reset game to initial state"""
        # Reset player
        road_left, road_right = self.road.get_boundaries()
        start_x = SCREEN_WIDTH // 2 - PLAYER_CAR_WIDTH // 2
        start_y = SCREEN_HEIGHT - PLAYER_CAR_HEIGHT - 20
        self.player.reset(start_x, start_y)
        
        # Clear obstacles and particles
        self.obstacles.clear()
        self.particles.clear()
        
        # Reset game variables
        self.score = 0
        self.spawn_timer = 0
        self.spawn_delay = INITIAL_SPAWN_DELAY
        self.last_milestone = 0
        
        # Reset road
        self.road.reset()
        
    def spawn_obstacle(self):
        """Spawn a new obstacle car"""
        road_left, road_right = self.road.get_boundaries()
        obstacle = ObstacleCar(road_left, road_right)
        self.obstacles.append(obstacle)
        
    def handle_difficulty_progression(self):
        """Increase difficulty as score increases"""
        for milestone in SCORE_MILESTONES:
            if self.score >= milestone and self.last_milestone < milestone:
                self.last_milestone = milestone
                
                # Increase speeds
                self.player.increase_difficulty(SPEED_INCREASE_PER_MILESTONE)
                self.road.increase_speed(SPEED_INCREASE_PER_MILESTONE * 0.5)
                
                # Increase obstacle speed
                for obstacle in self.obstacles:
                    obstacle.increase_speed(SPEED_INCREASE_PER_MILESTONE)
                
                print(f"Difficulty increased at score {milestone}!")
                
    def update_game(self):
        """Update game logic"""
        if not self.state_manager.is_playing():
            return
            
        # Update road animation
        self.road.update()
        
        # Update player
        self.player.update()
        
        # Emit exhaust particles
        exhaust_x = self.player.x + self.player.width // 2
        exhaust_y = self.player.y + self.player.height
        self.particles.emit_exhaust(exhaust_x, exhaust_y, self.player.boost_active)
        
        if self.player.boost_active:
            self.particles.emit_boost_trail(exhaust_x - 10, exhaust_y)
            self.particles.emit_boost_trail(exhaust_x + 10, exhaust_y)
        
        # Spawn obstacles
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_obstacle()
            self.spawn_timer = 0
            
            # Gradually decrease spawn delay (increase difficulty)
            if self.spawn_delay > MIN_SPAWN_DELAY:
                self.spawn_delay -= SPAWN_DELAY_DECREASE
        
        # Update obstacles
        road_left, road_right = self.road.get_boundaries()
        for obstacle in self.obstacles[:]:
            obstacle.move()
            
            # Remove off-screen obstacles
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.score += 1
                self.sound_manager.play_score()
                
            # Check collision
            if self.collision_detector.check_precise_collision(
                self.player.get_rect(), 
                obstacle.get_rect()
            ):
                # Game over
                collision_point = self.collision_detector.get_collision_point(
                    self.player.get_rect(),
                    obstacle.get_rect()
                )
                if collision_point:
                    self.particles.emit_collision_sparks(*collision_point)
                
                self.sound_manager.play_collision()
                self.state_manager.change_state(GameState.GAME_OVER)
        
        # Update particles
        self.particles.update()
        
        # Handle difficulty progression
        self.handle_difficulty_progression()
        
    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            # Menu state events
            if self.state_manager.is_menu():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    action = self.menu.handle_click(
                        pygame.mouse.get_pos(),
                        pygame.mouse.get_pressed()
                    )
                    if action == "start":
                        self.reset_game()
                        self.state_manager.change_state(GameState.PLAYING)
                    elif action == "quit":
                        self.running = False
                        
            # Playing state events
            elif self.state_manager.is_playing():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.activate_boost()
                        self.sound_manager.play_boost()
                    elif event.key == pygame.K_p:
                        self.state_manager.toggle_pause()
                    elif event.key == pygame.K_ESCAPE:
                        self.state_manager.change_state(GameState.MENU)
                        
            # Paused state events
            elif self.state_manager.is_paused():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.state_manager.toggle_pause()
                    elif event.key == pygame.K_ESCAPE:
                        self.state_manager.change_state(GameState.MENU)
                        
            # Game over state events
            elif self.state_manager.is_game_over():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state_manager.change_state(GameState.PLAYING)
                    elif event.key == pygame.K_ESCAPE:
                        self.state_manager.change_state(GameState.MENU)
        
        # Continuous key presses (for smooth movement)
        if self.state_manager.is_playing():
            keys = pygame.key.get_pressed()
            road_left, road_right = self.road.get_boundaries()
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left(road_left)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right(road_right)
                
    def render(self):
        """Render all game objects"""
        # Menu state
        if self.state_manager.is_menu():
            self.menu.draw(self.screen)
            self.menu.update(pygame.mouse.get_pos())
            
        # Playing or paused state
        elif self.state_manager.is_playing() or self.state_manager.is_paused():
            # Draw road
            self.road.draw(self.screen)
            
            # Draw particles (background layer)
            self.particles.draw(self.screen)
            
            # Draw obstacles
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
            
            # Draw player
            self.player.draw(self.screen)
            
            # Draw HUD
            self.hud.draw_playing_hud(
                self.screen,
                self.score,
                self.player.speed,
                self.player.boost_active
            )
            
            # Draw pause overlay if paused
            if self.state_manager.is_paused():
                self.hud.draw_pause_screen(self.screen)
                
        # Game over state
        elif self.state_manager.is_game_over():
            # Draw final frame
            self.road.draw(self.screen)
            self.particles.draw(self.screen)
            
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
            
            self.player.draw(self.screen)
            
            # Draw game over overlay
            self.hud.draw_game_over(self.screen, self.score)
        
        # Update display
        pygame.display.flip()
        
    def run(self):
        """Main game loop"""
        while self.running:
            # Limit frame rate
            self.clock.tick(FPS)
            
            # Handle events
            self.handle_events()
            
            # Update game state
            self.update_game()
            
            # Render everything
            self.render()
        
        # Cleanup
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game"""
    game = F1RacingGame()
    game.run()


if __name__ == "__main__":
    main()
