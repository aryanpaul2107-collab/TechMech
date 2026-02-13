"""
Menu System
Main menu and menu components
"""

import pygame
from config import *


class Button:
    """Interactive menu button"""
    
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        
    def draw(self, screen):
        """Draw the button"""
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=10)
        
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_hovered(self, mouse_pos):
        """Check if mouse is hovering over button"""
        return self.rect.collidepoint(mouse_pos)
    
    def update(self, mouse_pos):
        """Update button appearance based on hover"""
        self.current_color = self.hover_color if self.is_hovered(mouse_pos) else self.color
        
    def is_clicked(self, mouse_pos, mouse_pressed):
        """Check if button is clicked"""
        return self.is_hovered(mouse_pos) and mouse_pressed[0]


class MainMenu:
    """Main menu screen"""
    
    def __init__(self):
        self.title_font = pygame.font.Font(None, 80)
        self.subtitle_font = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        
        # Create buttons
        button_x = SCREEN_WIDTH // 2 - MENU_BUTTON_WIDTH // 2
        button_start_y = SCREEN_HEIGHT // 2
        
        self.start_button = Button(
            button_x, button_start_y,
            MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT,
            "START RACE", BLUE, DARKER_BLUE
        )
        
        self.instructions_button = Button(
            button_x, button_start_y + MENU_BUTTON_HEIGHT + MENU_BUTTON_SPACING,
            MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT,
            "CONTROLS", DARK_GRAY, GRAY
        )
        
        self.quit_button = Button(
            button_x, button_start_y + (MENU_BUTTON_HEIGHT + MENU_BUTTON_SPACING) * 2,
            MENU_BUTTON_WIDTH, MENU_BUTTON_HEIGHT,
            "QUIT", RED, (200, 0, 0)
        )
        
        self.buttons = [self.start_button, self.instructions_button, self.quit_button]
        self.show_instructions = False
        
    def draw(self, screen):
        """Draw the main menu"""
        # Background
        screen.fill(GRASS_GREEN)
        
        # Draw road in background
        road_left = (SCREEN_WIDTH - ROAD_WIDTH) // 2
        pygame.draw.rect(screen, ROAD_GRAY, (road_left, 0, ROAD_WIDTH, SCREEN_HEIGHT))
        
        # Title
        title_text = self.title_font.render("F1 RACING", True, YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        
        # Title shadow
        shadow_text = self.title_font.render("F1 RACING", True, BLACK)
        screen.blit(shadow_text, (title_rect.x + 3, title_rect.y + 3))
        screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_text = self.subtitle_font.render("Challenge Edition", True, WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, 220))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Draw buttons
        for button in self.buttons:
            button.draw(screen)
            
        # Show instructions if toggled
        if self.show_instructions:
            self._draw_instructions_overlay(screen)
            
    def _draw_instructions_overlay(self, screen):
        """Draw instructions overlay"""
        # Semi-transparent background
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Instructions box
        box_width = 500
        box_height = 350
        box_x = SCREEN_WIDTH // 2 - box_width // 2
        box_y = SCREEN_HEIGHT // 2 - box_height // 2
        
        pygame.draw.rect(screen, DARK_BLUE, (box_x, box_y, box_width, box_height), border_radius=15)
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height), 3, border_radius=15)
        
        # Title
        title_text = self.subtitle_font.render("CONTROLS", True, YELLOW)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, box_y + 40))
        screen.blit(title_text, title_rect)
        
        # Instructions
        instructions = [
            "← / A - Move Left",
            "→ / D - Move Right",
            "SPACE - Speed Boost",
            "P - Pause Game",
            "ESC - Return to Menu",
            "",
            "Avoid traffic and survive as long as possible!",
            "Your score increases as you pass cars."
        ]
        
        small_font = pygame.font.Font(None, FONT_SIZE_SMALL)
        y_offset = box_y + 80
        
        for instruction in instructions:
            text = small_font.render(instruction, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 30
            
        # Close instruction
        close_text = small_font.render("Click anywhere to close", True, LIGHT_GRAY)
        close_rect = close_text.get_rect(center=(SCREEN_WIDTH // 2, box_y + box_height - 30))
        screen.blit(close_text, close_rect)
        
    def update(self, mouse_pos):
        """Update menu buttons"""
        for button in self.buttons:
            button.update(mouse_pos)
            
    def handle_click(self, mouse_pos, mouse_pressed):
        """Handle button clicks and return action"""
        if self.show_instructions:
            # Close instructions on any click
            if mouse_pressed[0]:
                self.show_instructions = False
            return None
            
        if self.start_button.is_clicked(mouse_pos, mouse_pressed):
            return "start"
        elif self.instructions_button.is_clicked(mouse_pos, mouse_pressed):
            self.show_instructions = True
            return None
        elif self.quit_button.is_clicked(mouse_pos, mouse_pressed):
            return "quit"
        
        return None

 self.music_toggle = MusicToggleButton(
    x=SCREEN_WIDTH - 150,
    y=20,
    width=120,
    height=50
 )

 # In draw():
 self.music_toggle.draw(screen)

 # In handle_click():
 if self.music_toggle.handle_click(mouse_pos, mouse_pressed):
    sound_manager.enabled = self.music_toggle.get_state()
