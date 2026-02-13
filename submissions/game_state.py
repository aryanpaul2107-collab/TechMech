"""
Game State Manager
Handles different game states (Menu, Playing, Paused, Game Over)
"""

from enum import Enum


class GameState(Enum):
    """Enumeration of possible game states"""
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class GameStateManager:
    """Manages transitions between game states"""
    
    def __init__(self):
        self.current_state = GameState.MENU
        self.previous_state = None
        
    def change_state(self, new_state):
        """Change to a new game state"""
        self.previous_state = self.current_state
        self.current_state = new_state
        
    def is_menu(self):
        """Check if in menu state"""
        return self.current_state == GameState.MENU
    
    def is_playing(self):
        """Check if in playing state"""
        return self.current_state == GameState.PLAYING
    
    def is_paused(self):
        """Check if in paused state"""
        return self.current_state == GameState.PAUSED
    
    def is_game_over(self):
        """Check if in game over state"""
        return self.current_state == GameState.GAME_OVER
    
    def toggle_pause(self):
        """Toggle between playing and paused"""
        if self.current_state == GameState.PLAYING:
            self.change_state(GameState.PAUSED)
        elif self.current_state == GameState.PAUSED:
            self.change_state(GameState.PLAYING)
            
    def get_current_state(self):
        """Get current game state"""
        return self.current_state
      
