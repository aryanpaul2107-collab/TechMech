"""
HUD (Heads-Up Display)
Displays game information like score, speed, and status
"""

import pygame
from config import *


class HUD:
    """Heads-up display for game information"""
    
    def __init__(self):
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.high_score = 0
        
    def draw_playing_hud(self, screen, score, speed, boost_active):
        """Draw HUD during gameplay"""
        # Score display
        score_text = self.font_medium.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (HUD_PADDING, HUD_PADDING))
        
        # High score
        if score > self.high_score:
            self.high_score = score
        high_score_text = self.font_small.render(f"Best: {self.high_score}", True, YELLOW)
        screen.blit(high_score_text, (HUD_PADDING, HUD_PADDING + 40))
        
        # Speed indicator
        speed_text = self.font_small.render(f"Speed: {int(speed * 10)} km/h", True, WHITE)
        screen.blit(speed_text, (SCREEN_WIDTH - 150, HUD_PADDING))
        
        # Boost indicator
        if boost_active:
            boost_text = self.font_medium.render("BOOST!", True, YELLOW)
            text_rect = boost_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
            # Pulsing effect
            pygame.draw.rect(screen, (255, 255, 0, 100), text_rect.inflate(20, 10))
            screen.blit(boost_text, text_rect)
        
        # Controls hint (small)
        controls_text = self.font_small.render("← → : Move  |  SPACE: Boost  |  P: Pause", 
                                               True, LIGHT_GRAY)
        screen.blit(controls_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 25))
        
    def draw_game_over(self, screen, final_score):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font_large.render("GAME OVER!", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Final Score: {final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        # High score notification
        if final_score >= self.high_score:
            new_record_text = self.font_medium.render("NEW RECORD!", True, YELLOW)
            new_record_rect = new_record_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(new_record_text, new_record_rect)
        
        # Restart instructions
        restart_text = self.font_small.render("Press SPACE to restart  |  ESC for menu", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(restart_text, restart_rect)
        
    def draw_pause_screen(self, screen):
        """Draw pause screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Paused text
        paused_text = self.font_large.render("PAUSED", True, YELLOW)
        paused_rect = paused_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(paused_text, paused_rect)
        
        # Resume instructions
        resume_text = self.font_medium.render("Press P to resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(resume_text, resume_rect)
        
        # Menu option
        menu_text = self.font_small.render("Press ESC for main menu", True, LIGHT_GRAY)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        screen.blit(menu_text, menu_rect)
    
    def reset_high_score(self):
        """Reset high score (for testing)"""
        self.high_score = 0
