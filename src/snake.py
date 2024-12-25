import pygame
from config import CELL_SIZE, SHIELD_SPRITES, WIDTH, HEIGHT
from effects import BloodSplatter

class Snake:
    def __init__(self, player_sprite, x, y, is_enemy=False):
        self.body = [[x, y]]
        self.direction = (0, 1)  # Default movement
        self.grow = False
        self.alive = True
        self.is_enemy = is_enemy
        self.sprite_sheet = pygame.image.load(player_sprite).convert_alpha()
        self.sprite_timer = 0
        self.tongue_state = 0

        # Shield attributes
        self.shield_active = False
        self.shield_timer = 0
        self.shield_sprites = {
            "active": pygame.image.load(SHIELD_SPRITES["active"]).convert_alpha(),
            "hit": pygame.image.load(SHIELD_SPRITES["hit"]).convert_alpha()
        }

        # Load sprite parts
        self.head_sprites = [self.get_sprite(0, 0), self.get_sprite(0, 64)]  # Tongue in and out
        self.body_sprite = self.get_sprite(64, 0)
        self.turn_sprite = self.get_sprite(128, 0)
        self.tail_sprite = self.get_sprite(192, 0)

        # Debugging: Print sprite dimensions
        print(f"Head sprite size: {self.head_sprites[0].get_size()}")
        print(f"Body sprite size: {self.body_sprite.get_size()}")

    def get_sprite(self, x, y):
        """Extract individual sprites from the sprite sheet."""
        sprite = pygame.Surface((64, 64), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return pygame.transform.scale(sprite, (CELL_SIZE, CELL_SIZE))

    def activate_shield(self, duration):
        """Activate the shield for a set duration."""
        self.shield_active = True
        self.shield_timer = duration

    def update_shield(self):
        """Update the shield's timer and visuals."""
        if self.shield_active:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.shield_active = False

    def move(self):
        if not self.alive:
            return
        head_x, head_y = self.body[0]
        new_head = [head_x + self.direction[0] * CELL_SIZE, head_y + self.direction[1] * CELL_SIZE]

        # Constrain the snake within the game window boundaries
        new_head[0] = max(0, min(new_head[0], WIDTH - CELL_SIZE))
        new_head[1] = max(0, min(new_head[1], HEIGHT - CELL_SIZE))

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
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
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

        # Draw shield if active
        if self.shield_active:
            shield_sprite = (
                self.shield_sprites["hit"] if self.shield_timer % 10 < 5 else self.shield_sprites["active"]
            )
            surface.blit(shield_sprite, (self.body[0][0], self.body[0][1]))

        # Draw head with tongue animation
        head_x, head_y = self.body[0]
        surface.blit(self.head_sprites[self.tongue_state], (head_x, head_y))

        # Draw body segments
        for segment in self.body[1:]:
            segment_x, segment_y = segment
            surface.blit(self.body_sprite, (segment_x, segment_y))

    def take_damage(self, damage, blood_splatters, sprite_sheet, cell_size):
        """Handle snake taking damage."""
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            # Create blood splatter
            head_x, head_y = self.body[0]  # Get snake head position
            blood_splatter = BloodSplatter(head_x, head_y, sprite_sheet, cell_size)
            blood_splatters.append(blood_splatter)
