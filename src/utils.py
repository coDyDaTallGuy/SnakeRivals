## File: utils.py
import pygame
import random

# Utility Functions

def load_and_resize_image(image_path, cell_size):
    """Load an image and resize it to match the CELL_SIZE."""
    image = pygame.image.load(image_path).convert_alpha()
    return pygame.transform.scale(image, (cell_size, cell_size))

def wrap_around(position, grid_width, grid_height):
    """Wrap around the position when it exceeds grid boundaries."""
    x, y = position
    x = x % grid_width
    y = y % grid_height
    return x, y

def is_position_valid(position, grid_width, grid_height):
    """Check if a position is within the valid grid boundaries."""
    x, y = position
    return 0 <= x < grid_width and 0 <= y < grid_height

def get_random_position(grid_width, grid_height, cell_size):
    """Generate a random position within the grid, aligned to CELL_SIZE."""
    x = random.randint(0, grid_width - 1) * cell_size
    y = random.randint(0, grid_height - 1) * cell_size
    return x, y

def draw_text(surface, text, font, color, x, y):
    """Draw text on a surface at the specified position."""
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def check_collision(pos1, pos2, tolerance=0):
    """Check if two positions collide within a certain tolerance."""
    return abs(pos1[0] - pos2[0]) <= tolerance and abs(pos1[1] - pos2[1]) <= tolerance

def load_animation_frames(sprite_sheet_path, frame_width, frame_height):
    """Extract animation frames from a sprite sheet."""
    sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
    sheet_width, sheet_height = sprite_sheet.get_size()
    frames = []

    for y in range(0, sheet_height, frame_height):
        for x in range(0, sheet_width, frame_width):
            frame = sprite_sheet.subsurface((x, y, frame_width, frame_height))
            frames.append(frame)

    return frames

def calculate_distance(pos1, pos2):
    """Calculate the distance between two points."""
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

def timer(countdown, callback):
    """Utility for managing countdown timers with a callback."""
    if countdown > 0:
        return countdown - 1
    else:
        callback()
        return 0
