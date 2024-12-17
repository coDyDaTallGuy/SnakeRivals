## File: powerups.py
import random
import pygame
from config import WIDTH, HEIGHT, CELL_SIZE, PURPLE

class PowerUp:
    def __init__(self):
        self.position = [random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
        self.color = PURPLE
        self.effect = random.choice(["speed", "shrink", "invincible"])

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
