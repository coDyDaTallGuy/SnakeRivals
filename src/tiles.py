## File: tiles.py
import pygame
from config import CELL_SIZE

class Tile:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.position = position  # Position as (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE))


class TileMap:
    def __init__(self, map_data, tileset):
        """
        :param map_data: 2D list representing the map (tile IDs).
        :param tileset: Dictionary mapping tile IDs to image paths.
        """
        self.tiles = []
        for y, row in enumerate(map_data):
            for x, tile_id in enumerate(row):
                if tile_id in tileset:
                    tile = Tile(tileset[tile_id], (x, y))
                    self.tiles.append(tile)

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)
