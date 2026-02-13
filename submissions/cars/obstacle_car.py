"""
Obstacle Car Class
Handles AI-controlled cars that the player must avoid
"""

import pygame
import random
from config import *


class ObstacleCar:
    """AI-controlled obstacle car"""
    
    def __init__(self, road_left, road_right):
        self.width = OBSTACLE_CAR_WIDTH
        self.height = OBSTACLE_CAR_HEIGHT
        self.x = random.randint(road_left, road_right - self.width)
        self.y = -self.height
        self.speed = OBSTACLE_CAR_SPEED
        self.color = random.choice(OBSTACLE_CAR_COLORS)
        self.car_type = random.choice(['sedan', 'sports', 'suv'])
        
    def draw(self, screen):
        """Draw the obstacle car based on its type"""
        if self.car_type == 'sports':
            self._draw_sports_car(screen)
        elif self.car_type == 'suv':
            self._draw_suv(screen)
        else:
            self._draw_sedan(screen)
            
    def _draw_sedan(self, screen):
        """Draw a sedan style car"""
        # Main car body
        pygame.draw.rect(screen, self.color, (self.x + 5, self.y + 5, self.width - 10, self.height - 25))
        
        # Car rear (back bumper area)
        rear_points = [
            (self.x + 10, self.y + self.height - 20),
            (self.x + self.width - 10, self.y + self.height - 20),
            (self.x + self.width - 5, self.y + self.height - 5),
            (self.x + 5, self.y + self.height - 5)
        ]
        pygame.draw.polygon(screen, self.color, rear_points)
        
        # Rear window
        rear_window_points = [
            (self.x + 10, self.y + self.height - 20),
            (self.x + self.width - 10, self.y + self.height - 20),
            (self.x + self.width - 15, self.y + self.height - 35),
            (self.x + 15, self.y + self.height - 35)
        ]
        pygame.draw.polygon(screen, (100, 100, 150), rear_window_points)
        
        # Front windshield
        pygame.draw.rect(screen, (100, 100, 150), (self.x + 12, self.y + 10, self.width - 24, 15))
        
        # Wheels
        self._draw_wheels(screen)
        
        # Brake lights
        pygame.draw.rect(screen, (150, 0, 0), (self.x + 8, self.y + self.height - 8, 8, 3))
        pygame.draw.rect(screen, (150, 0, 0), (self.x + self.width - 16, self.y + self.height - 8, 8, 3))
        
        # Roof detail
        darker_color = (max(0, self.color[0] - 30),
                       max(0, self.color[1] - 30),
                       max(0, self.color[2] - 30))
        pygame.draw.rect(screen, darker_color, (self.x + 15, self.y + 30, self.width - 30, 20))
    
    def _draw_sports_car(self, screen):
        """Draw a sports car style (lower, sleeker)"""
        # Main body - lower profile
        pygame.draw.rect(screen, self.color, (self.x + 3, self.y + 10, self.width - 6, self.height - 30))
        
        # Sloped rear
        rear_points = [
            (self.x + 8, self.y + self.height - 20),
            (self.x + self.width - 8, self.y + self.height - 20),
            (self.x + self.width - 3, self.y + self.height - 5),
            (self.x + 3, self.y + self.height - 5)
        ]
        pygame.draw.polygon(screen, self.color, rear_points)
        
        # Windshield - more angled
        pygame.draw.polygon(screen, (80, 80, 120), [
            (self.x + 10, self.y + 15),
            (self.x + self.width - 10, self.y + 15),
            (self.x + self.width - 12, self.y + 25),
            (self.x + 12, self.y + 25)
        ])
        
        # Spoiler
        pygame.draw.rect(screen, BLACK, (self.x + 8, self.y + self.height - 22, self.width - 16, 2))
        
        # Wheels
        self._draw_wheels(screen)
        
        # Racing stripe
        pygame.draw.rect(screen, WHITE, (self.x + self.width // 2 - 2, self.y + 8, 4, self.height - 18))
        
    def _draw_suv(self, screen):
        """Draw an SUV style (taller, boxier)"""
        # Main body - taller
        pygame.draw.rect(screen, self.color, (self.x + 5, self.y + 3, self.width - 10, self.height - 20))
        
        # Rear
        pygame.draw.rect(screen, self.color, (self.x + 5, self.y + self.height - 17, self.width - 10, 12))
        
        # Windows
        pygame.draw.rect(screen, (90, 90, 130), (self.x + 10, self.y + 8, self.width - 20, 15))
        pygame.draw.rect(screen, (90, 90, 130), (self.x + 10, self.y + 35, self.width - 20, 20))
        
        # Wheels - larger for SUV
        pygame.draw.ellipse(screen, BLACK, (self.x - 4, self.y + 8, 12, 22))
        pygame.draw.ellipse(screen, GRAY, (self.x - 2, self.y + 10, 8, 18))
        
        pygame.draw.ellipse(screen, BLACK, (self.x + self.width - 8, self.y + 8, 12, 22))
        pygame.draw.ellipse(screen, GRAY, (self.x + self.width - 6, self.y + 10, 8, 18))
        
        pygame.draw.ellipse(screen, BLACK, (self.x - 4, self.y + 50, 12, 22))
        pygame.draw.ellipse(screen, GRAY, (self.x - 2, self.y + 52, 8, 18))
        
        pygame.draw.ellipse(screen, BLACK, (self.x + self.width - 8, self.y + 50, 12, 22))
        pygame.draw.ellipse(screen, GRAY, (self.x + self.width - 6, self.y + 52, 8, 18))
        
        # Roof rack
        pygame.draw.rect(screen, DARK_GRAY, (self.x + 8, self.y + 5, self.width - 16, 2))
        
    def _draw_wheels(self, screen):
        """Draw standard wheels for sedan and sports cars"""
        # Front left
        pygame.draw.rect(screen, BLACK, (self.x - 3, self.y + 10, 8, 18), border_radius=3)
        pygame.draw.circle(screen, GRAY, (self.x + 1, self.y + 19), 3)
        # Front right
        pygame.draw.rect(screen, BLACK, (self.x + self.width - 5, self.y + 10, 8, 18), border_radius=3)
        pygame.draw.circle(screen, GRAY, (self.x + self.width - 1, self.y + 19), 3)
        # Rear left
        pygame.draw.rect(screen, BLACK, (self.x - 3, self.y + 52, 8, 18), border_radius=3)
        pygame.draw.circle(screen, GRAY, (self.x + 1, self.y + 61), 3)
        # Rear right
        pygame.draw.rect(screen, BLACK, (self.x + self.width - 5, self.y + 52, 8, 18), border_radius=3)
        pygame.draw.circle(screen, GRAY, (self.x + self.width - 1, self.y + 61), 3)
        
    def move(self):
        """Move the car down the screen"""
        self.y += self.speed
        
    def is_off_screen(self):
        """Check if car has moved off screen"""
        return self.y > SCREEN_HEIGHT
    
    def increase_speed(self, amount):
        """Increase car speed for difficulty progression"""
        self.speed += amount
        
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
