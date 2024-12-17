## File: food.py
import random
import pygame
from config import WIDTH, HEIGHT, CELL_SIZE, FOOD_SPRITE

class Food:
    def __init__(self):
        self.position = [random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
        self.sprite = pygame.image.load(FOOD_SPRITE)

    def draw(self, surface):
        surface.blit(self.sprite, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
