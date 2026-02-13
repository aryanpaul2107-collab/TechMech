"""
Road Class
Handles the racing track rendering and animation
"""

import pygame
from config import *


class Road:
    """Animated racing road/track"""
    
    def __init__(self):
        self.width = ROAD_WIDTH
        self.speed = ROAD_SPEED
        self.line_offset = 0
        self.left_boundary = (SCREEN_WIDTH - self.width) // 2
        self.right_boundary = (SCREEN_WIDTH + self.width) // 2
        
    def draw(self, screen):
        """Draw the road with animated lane markings"""
        # Grass background
        screen.fill(GRASS_GREEN)
        
        # Road surface
        pygame.draw.rect(screen, ROAD_GRAY, 
                        (self.left_boundary, 0, self.width, SCREEN_HEIGHT))
        
        # Road edges (white lines)
        pygame.draw.rect(screen, WHITE, 
                        (self.left_boundary, 0, ROAD_EDGE_WIDTH, SCREEN_HEIGHT))
        pygame.draw.rect(screen, WHITE, 
                        (self.right_boundary - ROAD_EDGE_WIDTH, 0, ROAD_EDGE_WIDTH, SCREEN_HEIGHT))
        
        # Center line (animated dashed line)
        self._draw_center_line(screen)
        
        # Optional: Lane dividers
        self._draw_lane_dividers(screen)
        
    def _draw_center_line(self, screen):
        """Draw animated center line"""
        center_x = SCREEN_WIDTH // 2 - 5
        
        for y in range(int(self.line_offset), SCREEN_HEIGHT, ROAD_LINE_HEIGHT + ROAD_LINE_GAP):
            pygame.draw.rect(screen, YELLOW, 
                           (center_x, y, 10, ROAD_LINE_HEIGHT))
    
    def _draw_lane_dividers(self, screen):
        """Draw additional lane dividers for realism"""
        # Left lane divider
        left_divider_x = self.left_boundary + self.width // 3
        # Right lane divider
        right_divider_x = self.left_boundary + 2 * self.width // 3
        
        for y in range(int(self.line_offset), SCREEN_HEIGHT, ROAD_LINE_HEIGHT + ROAD_LINE_GAP):
            # Left divider
            pygame.draw.rect(screen, WHITE, 
                           (left_divider_x, y, 6, ROAD_LINE_HEIGHT // 2))
            # Right divider
            pygame.draw.rect(screen, WHITE, 
                           (right_divider_x, y, 6, ROAD_LINE_HEIGHT // 2))
            
    def update(self):
        """Update road animation"""
        self.line_offset += self.speed
        if self.line_offset >= ROAD_LINE_HEIGHT + ROAD_LINE_GAP:
            self.line_offset = 0
            
    def increase_speed(self, amount):
        """Increase road speed for difficulty progression"""
        self.speed += amount
        
    def get_boundaries(self):
        """Get left and right road boundaries"""
        return self.left_boundary, self.right_boundary
    
    def reset(self):
        """Reset road to initial state"""
        self.speed = ROAD_SPEED
        self.line_offset = 0
