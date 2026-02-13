"""
Player F1 Car Class
Handles the player-controlled Formula 1 race car
"""

import pygame
from config import *


class PlayerCar:
    """Formula 1 race car controlled by the player"""
    
    def __init__(self, x, y):
        self.width = PLAYER_CAR_WIDTH
        self.height = PLAYER_CAR_HEIGHT
        self.x = x
        self.y = y
        self.speed = PLAYER_CAR_SPEED
        self.base_speed = PLAYER_CAR_SPEED
        self.color = PLAYER_CAR_COLOR
        self.boost_active = False
        self.boost_timer = 0
        
    def draw(self, screen):
        """Draw the F1 car with all details"""
        
        # Nose cone (pointed front)
        nose_points = [
            (self.x + self.width // 2, self.y),  # tip
            (self.x + 5, self.y + 15),
            (self.x + self.width - 5, self.y + 15)
        ]
        pygame.draw.polygon(screen, self.color, nose_points)
        
        # Front wing
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 12, self.width + 10, 3))
        pygame.draw.rect(screen, self.color, (self.x - 3, self.y + 10, self.width + 6, 2))
        
        # Side pods (main body)
        # Left side pod
        pygame.draw.rect(screen, self.color, (self.x + 3, self.y + 15, 15, 45))
        pygame.draw.rect(screen, DARK_BLUE, (self.x + 5, self.y + 18, 11, 40))
        # Right side pod
        pygame.draw.rect(screen, self.color, (self.x + self.width - 18, self.y + 15, 15, 45))
        pygame.draw.rect(screen, DARK_BLUE, (self.x + self.width - 16, self.y + 18, 11, 40))
        
        # Center cockpit area
        cockpit_points = [
            (self.x + 20, self.y + 20),
            (self.x + self.width - 20, self.y + 20),
            (self.x + self.width - 20, self.y + 45),
            (self.x + 20, self.y + 45)
        ]
        pygame.draw.polygon(screen, DARKER_BLUE, cockpit_points)
        
        # Driver helmet/cockpit
        pygame.draw.ellipse(screen, YELLOW, (self.x + 18, self.y + 25, 14, 14))
        pygame.draw.rect(screen, (50, 50, 50), (self.x + 20, self.y + 28, 10, 6))  # visor
        
        # Air intake
        pygame.draw.rect(screen, BLACK, (self.x + self.width // 2 - 4, self.y + 22, 8, 18))
        pygame.draw.rect(screen, (30, 30, 30), (self.x + self.width // 2 - 3, self.y + 23, 6, 16))
        
        # Rear wing support
        pygame.draw.rect(screen, BLACK, (self.x + 12, self.y + 60, 3, 8))
        pygame.draw.rect(screen, BLACK, (self.x + self.width - 15, self.y + 60, 3, 8))
        
        # Rear wing (changes color if boost active)
        wing_color = YELLOW if self.boost_active else RED
        pygame.draw.rect(screen, wing_color, (self.x + 5, self.y + 66, self.width - 10, 4))
        pygame.draw.rect(screen, wing_color, (self.x + 5, self.y + 72, self.width - 10, 3))
        
        # Rear body/engine cover
        pygame.draw.rect(screen, self.color, (self.x + 10, self.y + 45, self.width - 20, 15))
        pygame.draw.rect(screen, DARK_BLUE, (self.x + 12, self.y + 47, self.width - 24, 11))
        
        # Exhaust pipes (glow if boost active)
        exhaust_color = ORANGE if self.boost_active else LIGHT_GRAY
        pygame.draw.circle(screen, exhaust_color, (self.x + 15, self.y + 63), 3)
        pygame.draw.circle(screen, exhaust_color, (self.x + self.width - 15, self.y + 63), 3)
        pygame.draw.circle(screen, DARK_GRAY, (self.x + 15, self.y + 63), 2)
        pygame.draw.circle(screen, DARK_GRAY, (self.x + self.width - 15, self.y + 63), 2)
        
        # F1 Wheels (larger, more exposed)
        self._draw_wheel(screen, self.x - 8, self.y + 12, 14, 20)
        self._draw_wheel(screen, self.x + self.width - 6, self.y + 12, 14, 20)
        self._draw_wheel(screen, self.x - 8, self.y + 48, 14, 22)
        self._draw_wheel(screen, self.x + self.width - 6, self.y + 48, 14, 22)
        
        # Racing number
        number_font = pygame.font.Font(None, 20)
        number = number_font.render("1", True, WHITE)
        screen.blit(number, (self.x + self.width // 2 - 4, self.y + 30))
        
        # Sponsor decals
        pygame.draw.rect(screen, RED, (self.x + 22, self.y + 50, 6, 3))
        pygame.draw.rect(screen, WHITE, (self.x + self.width - 28, self.y + 50, 6, 3))
        
    def _draw_wheel(self, screen, x, y, width, height):
        """Draw a single F1 wheel"""
        pygame.draw.ellipse(screen, BLACK, (x, y, width, height))
        pygame.draw.ellipse(screen, GRAY, (x + 2, y + 2, width - 4, height - 4))
        center_x = x + width // 2
        center_y = y + height // 2
        pygame.draw.circle(screen, DARK_GRAY, (center_x, center_y), 3)
        
    def move_left(self, road_left):
        """Move the car left within road boundaries"""
        self.x -= self.speed
        if self.x < road_left:
            self.x = road_left
            
    def move_right(self, road_right):
        """Move the car right within road boundaries"""
        self.x += self.speed
        if self.x > road_right - self.width:
            self.x = road_right - self.width
    
    def activate_boost(self):
        """Activate temporary speed boost"""
        self.boost_active = True
        self.boost_timer = 60  # 1 second at 60 FPS
        self.speed = self.base_speed * 1.5
        
    def update(self):
        """Update car state"""
        if self.boost_active:
            self.boost_timer -= 1
            if self.boost_timer <= 0:
                self.boost_active = False
                self.speed = self.base_speed
                
    def increase_difficulty(self, amount):
        """Increase car speed for difficulty progression"""
        self.base_speed += amount
        if not self.boost_active:
            self.speed = self.base_speed
            
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def reset(self, x, y):
        """Reset car to initial position"""
        self.x = x
        self.y = y
        self.speed = PLAYER_CAR_SPEED
        self.base_speed = PLAYER_CAR_SPEED
        self.boost_active = False
        self.boost_timer = 0
      
