## File: config.py
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

# Audio Files
MENU_SOUND = "sounds/menu.wav"
GAME_OVER_SOUND = "sounds/game_over.wav"
ATTACK_SOUND = "sounds/attack.wav"
FOOD_SOUND = "sounds/food.wav"

# Sprites
PLAYER_SPRITE = "sprites/snake_sprite_sheet.png"
ENEMY_SPRITE = "sprites/enemy.png"
FOOD_SPRITE = "sprites/food.png"
OBSTACLE_SPRITE = "sprites/obstacle.png"
GRASS_TILE = "sprites/grass_tile.png"
DIRT_TILE = "sprites/dirt_tile.png"
WATER_TILE = "sprites/water_tile.png"
STONE_TILE = "sprites/stone_tile.png"
SAND_TILE = "sprites/sand_tile.png"
LAVA_TILE = "sprites/lava_tile.png"
SNOW_TILE = "sprites/snow_tile.png"
BRICK_TILE = "sprites/brick_tile.png"

# Tileset
TILESET = {
    0: GRASS_TILE,
    1: DIRT_TILE,
    2: WATER_TILE,
    3: STONE_TILE,
    4: SAND_TILE,
    5: LAVA_TILE,
    6: SNOW_TILE,
    7: BRICK_TILE
}

# Default Settings
DEFAULT_WINDOW_SIZE = (800, 600)
DEFAULT_FPS = 15
DEFAULT_SNAKE_SPEED = 1
DEFAULT_SNAKE_COLOR = GREEN
DEFAULT_ENEMY_COLOR = RED
