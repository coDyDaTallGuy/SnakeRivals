## File: obstacles.py
import random
import pygame
from config import WIDTH, HEIGHT, CELL_SIZE, OBSTACLE_SPRITE

class Obstacle:
    def __init__(self, count=5):
        self.obstacles = []
        self.sprite = pygame.image.load(OBSTACLE_SPRITE)
        for _ in range(count):
            position = [random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            self.obstacles.append(position)

    def draw(self, surface):
        for position in self.obstacles:
            surface.blit(self.sprite, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

    def get_positions(self):
        return self.obstacles
