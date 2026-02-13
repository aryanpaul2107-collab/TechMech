# F1 Racing Challenge 🏎️

A high-speed Formula 1 racing game built with Python and Pygame. Test your reflexes as you navigate through traffic at breakneck speeds!

## 🎮 Features

- **Formula 1 Style Racing**: Detailed F1 car with realistic aerodynamic features
- **Dynamic Difficulty**: Game gets progressively harder as you score more points
- **Multiple Car Types**: Face sedans, sports cars, and SUVs as obstacles
- **Particle Effects**: Exhaust smoke, boost trails, and collision sparks
- **Speed Boost System**: Activate temporary speed boosts for intense moments
- **Professional UI**: Clean menu system with pause functionality
- **High Score Tracking**: Compete against your personal best
- **Smooth Controls**: Responsive keyboard controls for precise maneuvering

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.0 or higher

## 🚀 Installation

1. **Clone or download this repository**

2. **Install Pygame:**
```bash
pip install pygame
```

## 🎯 How to Play

### Starting the Game

```bash
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| ← / A | Move Left |
| → / D | Move Right |
| SPACE | Activate Speed Boost |
| P | Pause Game |
| ESC | Return to Menu |

### Objective

- Avoid incoming traffic for as long as possible
- Your score increases each time you successfully pass a car
- The game gets faster and more challenging as your score increases
- Try to beat your high score!

### Gameplay Tips

- Use the speed boost strategically to escape tight situations
- Watch the speed indicator to know how fast you're going
- The game increases difficulty at scores: 10, 25, 50, 100, 150, 200
- Stay centered to have maximum maneuverability in both directions

## 📁 Project Structure

```
car_racing_game/
├── main.py                 # Main game loop and orchestration
├── config.py              # Game constants and settings
├── cars/                  # Car-related classes
│   ├── __init__.py
│   ├── player_car.py      # F1 player car with boost mechanics
│   └── obstacle_car.py    # AI traffic cars (sedan, sports, SUV)
├── game/                  # Core game logic
│   ├── __init__.py
│   ├── road.py           # Road rendering and animation
│   ├── particle_effects.py  # Visual effects system
│   └── game_state.py     # Game state management
├── ui/                    # User interface components
│   ├── __init__.py
│   ├── hud.py            # Heads-up display
│   └── menu.py           # Main menu and buttons
├── utils/                 # Utility modules
│   ├── __init__.py
│   ├── collision.py      # Collision detection
│   └── sound_manager.py  # Sound system (placeholder)
└── assets/               # Game assets (future expansion)
    └── (sounds, images, etc.)
```

## 🎨 Customization

### Modify Game Difficulty

Edit values in `config.py`:

```python
# Make the game easier
PLAYER_CAR_SPEED = 10          # Increase player speed
OBSTACLE_CAR_SPEED = 5         # Decrease obstacle speed
INITIAL_SPAWN_DELAY = 80       # Increase time between obstacles

# Make the game harder
PLAYER_CAR_SPEED = 6           # Decrease player speed
OBSTACLE_CAR_SPEED = 9         # Increase obstacle speed
INITIAL_SPAWN_DELAY = 40       # Decrease time between obstacles
```

### Change Car Colors

In `config.py`:

```python
PLAYER_CAR_COLOR = BLUE        # Change to any RGB tuple
OBSTACLE_CAR_COLORS = [RED, GREEN, YELLOW, ORANGE]  # Add/remove colors
```

### Adjust Screen Size

```python
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
```

## 🔧 Technical Details

### Architecture

The game uses an object-oriented design with clear separation of concerns:

- **Model-View-Controller pattern**: Game logic, rendering, and input handling are separated
- **State Management**: Clean state transitions between menu, playing, paused, and game over
- **Component-based**: Each game element is its own class with specific responsibilities
- **Modular**: Easy to extend with new features or modify existing ones

### Key Classes

- `F1RacingGame`: Main orchestrator
- `PlayerCar`: F1 race car with boost mechanics
- `ObstacleCar`: AI traffic with multiple car types
- `Road`: Animated racing track
- `ParticleSystem`: Visual effects engine
- `GameStateManager`: State machine for game flow
- `HUD`: Information display
- `MainMenu`: Menu interface
- `CollisionDetector`: Precise collision detection

### Performance

- Runs at 60 FPS on most systems
- Efficient particle system with automatic cleanup
- Optimized collision detection with tolerance
- Minimal resource usage

## 🎵 Future Enhancements

Planned features for future versions:

- [ ] Sound effects and background music
- [ ] Multiple tracks/environments
- [ ] Power-ups (shields, magnets, etc.)
- [ ] Leaderboard system
- [ ] Different game modes (time trial, endless)
- [ ] Vehicle customization
- [ ] Weather effects
- [ ] Multiplayer support

## 🐛 Troubleshooting

### Game won't start
- Ensure Pygame is installed: `pip install pygame`
- Check Python version: `python --version` (needs 3.7+)

### Lag or low FPS
- Close other applications
- Reduce particle count in `config.py`
- Lower screen resolution

### Controls not responding
- Click on the game window to ensure it has focus
- Check if keys are working in other applications

## 📝 License

This project is free to use for educational and personal purposes.

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add new car types
- Create different road themes
- Implement power-up system
- Add sound effects
- Create new game modes

## 👨‍💻 Development

To extend the game:

1. Game logic goes in `game/` directory
2. New car types go in `cars/` directory
3. UI components go in `ui/` directory
4. Utility functions go in `utils/` directory
5. Constants and settings go in `config.py`

## 📞 Support

For issues or questions, please check:
- The troubleshooting section above
- Comments in the source code
- Pygame documentation: https://www.pygame.org/docs/

---

**Enjoy the race! 🏁**
