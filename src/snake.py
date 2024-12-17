## File: snake.py
import pygame
from config import PLAYER_SPRITE, CELL_SIZE

class Snake:
    def __init__(self, color, x, y, is_enemy=False):
        self.body = [[x, y]]
        self.direction = (0, 1)  # Default movement
        self.grow = False
        self.alive = True
        self.is_enemy = is_enemy
        self.sprite_sheet = pygame.image.load(PLAYER_SPRITE).convert_alpha()
        self.sprite_timer = 0
        self.tongue_state = 0

        # Load sprite parts
        self.head_sprites = [self.get_sprite(0, 0), self.get_sprite(0, 64)]  # Tongue in and out
        self.body_sprite = self.get_sprite(64, 0)
        self.turn_sprite = self.get_sprite(128, 0)
        self.tail_sprite = self.get_sprite(192, 0)

    def get_sprite(self, x, y):
        """Extract individual sprites from the sprite sheet."""
        sprite = pygame.Surface((64, 64), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return pygame.transform.scale(sprite, (CELL_SIZE, CELL_SIZE))

    def move(self):
        if not self.alive:
            return
        head_x, head_y = self.body[0]
        new_head = [head_x + self.direction[0] * CELL_SIZE, head_y + self.direction[1] * CELL_SIZE]
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        self.grow = False

        # Sprite timer for tongue animation
        self.sprite_timer = (self.sprite_timer + 1) % 10
        if self.sprite_timer == 0:
            self.tongue_state = 1 - self.tongue_state

    def check_collision(self, snakes, obstacles=[]):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= 800 or head_y < 0 or head_y >= 600:
            self.alive = False
        for snake in snakes:
            for segment in snake.body:
                if [head_x, head_y] == segment and snake != self:
                    self.alive = False
        for obstacle in obstacles:
            if [head_x, head_y] == obstacle:
                self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
        # Draw head with tongue animation
        head_x, head_y = self.body[0]
        surface.blit(self.head_sprites[self.tongue_state], (head_x, head_y))

        # Draw body segments
        for i, segment in enumerate(self.body[1:], 1):
            segment_x, segment_y = segment
            surface.blit(self.body_sprite, (segment_x, segment_y))
