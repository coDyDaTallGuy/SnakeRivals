import os

# Game Settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 64
FPS = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Base directory is two levels up from the current file's location (assuming 'src' is in 'SnakeRivals')
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

# Fonts
FONTS = {
    "title": os.path.join(FONTS_DIR, "TrajanPro-Regular.ttf"),
    "subtitle": os.path.join(FONTS_DIR, "DecoratedRomanInitials.ttf"),
    "score": os.path.join(FONTS_DIR, "macedonia.3d-filled-regular.ttf"),
}

# Audio Files
MENU_SOUND = os.path.join(SOUNDS_DIR, "menu.wav")
GAME_OVER_SOUND = os.path.join(SOUNDS_DIR, "game_over.wav")
ATTACK_SOUND = os.path.join(SOUNDS_DIR, "attack.wav")
FOOD_SOUND = os.path.join(SOUNDS_DIR, "food.ogg")
POWERUP_SOUND = os.path.join(SOUNDS_DIR, "powerup.wav")

# Tile Sprites 
GRASS_TILE = os.path.join(SPRITES_DIR, "grass_tile.png")
DIRT_TILE = os.path.join(SPRITES_DIR, "dirt_tile.png")
WATER_TILE = os.path.join(SPRITES_DIR, "water_tile.png")
STONE_TILE = os.path.join(SPRITES_DIR, "stone_tile.png")
SAND_TILE = os.path.join(SPRITES_DIR, "sand_tile.png")
LAVA_TILE = os.path.join(SPRITES_DIR, "lava_tile.png")
SNOW_TILE = os.path.join(SPRITES_DIR, "snow_tile.png")
BRICK_TILE = os.path.join(SPRITES_DIR, "brick_tile.png")

# Shield Sprites
SHIELD_SPRITES = {
    "active": os.path.join(SPRITES_DIR, "shieldOn.png"),
    "hit": os.path.join(SPRITES_DIR, "shieldGreen.png")
}

# Powerup Sprites
POWERUP_SPRITES = {
    "shield": os.path.join(SPRITES_DIR, "power_shield.png"),
    "speed": os.path.join(SPRITES_DIR, "power_speed.png"),
    "growth": os.path.join(SPRITES_DIR, "spinach.png"),
    "freeze": os.path.join(SPRITES_DIR, "snowflake.png"),
    "teleportation_start": os.path.join(SPRITES_DIR, "teleporter_hit.png"),
    "teleportation_end": os.path.join(SPRITES_DIR, "teleporter_01.png"),
    "midas": os.path.join(SPRITES_DIR, "power_midas.png"),
    "power": os.path.join(SPRITES_DIR, "power_power.png"),
    "teleportation": os.path.join(SPRITES_DIR, "teleporter_01.png")
}

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

# Snake Skins
SNAKE_SKINS = {
    "Green Snake": os.path.join(SPRITES_DIR, "snakes", "snake_green.png"),
    "Dark Blue Snake": os.path.join(SPRITES_DIR, "snakes", "snake_darkblue.png"),
    "Darkest Blue Snake": os.path.join(SPRITES_DIR, "snakes", "snake_darkestblue.png"),
    "Tannish Gold Snake": os.path.join(SPRITES_DIR, "snakes", "snake_tangold.png"),
    "Orange Snake": os.path.join(SPRITES_DIR, "snakes", "snake_orange.png"),
    "Red Snake": os.path.join(SPRITES_DIR, "snakes", "snake_red.png"),
    "Really Black Snake": os.path.join(SPRITES_DIR, "snakes", "snake_reallyblack.png")
}
