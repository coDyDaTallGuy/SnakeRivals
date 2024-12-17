## File: snake.py
import random
import pygame
from config import WIDTH, HEIGHT, CELL_SIZE, PLAYER_SPRITE, ENEMY_SPRITE

class Snake:
    def __init__(self, color, x, y, is_enemy=False):
        self.body = [[x, y]]
        self.color = color
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.grow = False
        self.is_enemy = is_enemy
        self.alive = True
        self.sprite = pygame.image.load(ENEMY_SPRITE if is_enemy else PLAYER_SPRITE)

    def move(self):
        if not self.alive:
            return
        head_x, head_y = self.body[0]
        new_head = [head_x + self.direction[0] * CELL_SIZE, head_y + self.direction[1] * CELL_SIZE]
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        self.grow = False

    def check_collision(self, snakes, obstacles=[]):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.alive = False
        for snake in snakes:
            for segment in snake.body:
                if [head_x, head_y] == segment and snake != self:
                    self.alive = False
        for obstacle in obstacles:
            if [head_x, head_y] == obstacle.position:
                self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
        for segment in self.body:
            surface.blit(self.sprite, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def attack(self, snakes):
        head_x, head_y = self.body[0]
        for snake in snakes:
            if snake.is_enemy and snake.alive:
                for segment in snake.body:
                    if [head_x, head_y] == segment:
                        snake.alive = False
                        return True
        return False
