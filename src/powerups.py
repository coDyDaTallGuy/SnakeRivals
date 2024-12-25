import pygame
import random
import os
from config import CELL_SIZE, SPRITES_DIR, POWERUP_SPRITES
from utils import load_animation_frames


class PowerUp:
    def __init__(self, x, y, effect, duration, image_path):
        self.position = (x, y)
        self.effect = effect
        self.duration = duration
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.active = False

    def draw(self, surface):
        if not self.active:
            surface.blit(self.image, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE))

    def activate(self, player, enemies):
        self.active = True
        self.effect(player, enemies)


class TeleportationEffect:
    """Handles the teleportation animation and logic."""

    def __init__(self, dematerialize_sprites, materialize_sprites, cell_size):
        self.dematerialize_frames = load_animation_frames(dematerialize_sprites, cell_size, cell_size)
        self.materialize_frames = load_animation_frames(materialize_sprites, cell_size, cell_size)
        self.frame_index = 0
        self.animating = False
        self.teleport_done = False

    def start_teleport(self):
        self.animating = True
        self.frame_index = 0
        self.teleport_done = False

    def update(self, surface, x, y):
        """Handle the animation."""
        if self.animating:
            if self.frame_index < len(self.dematerialize_frames):
                # Dematerialization phase
                surface.blit(self.dematerialize_frames[self.frame_index], (x, y))
            elif self.frame_index < len(self.dematerialize_frames) + len(self.materialize_frames):
                # Materialization phase
                mat_index = self.frame_index - len(self.dematerialize_frames)
                surface.blit(self.materialize_frames[mat_index], (x, y))
            else:
                self.animating = False
                self.teleport_done = True

            self.frame_index += 1


class PowerUpManager:
    def __init__(self, spawn_count):
        self.powerups = []
        self.spawn_count = spawn_count
        self.effects = {
            "speed": self.speed_boost,
            "shield": self.shield,
            "power": self.power_boost,
            "midas": self.midas_touch,
            "freeze": self.freeze_enemies,
            "growth": self.growth_boost,
            "teleportation": self.teleportation
        }
        self.images = POWERUP_SPRITES

        for _ in range(spawn_count):
            x, y = random.randint(0, 39), random.randint(0, 29)
            effect_name = random.choice(list(self.effects.keys()))
            powerup = PowerUp(x, y, self.effects[effect_name], duration=200, image_path=self.images[effect_name])
            self.powerups.append(powerup)

    def draw(self, surface):
        for powerup in self.powerups:
            powerup.draw(surface)

    def check_collisions(self, snake_head, enemies):
        for powerup in self.powerups:
            px, py = powerup.position
            if (px * CELL_SIZE, py * CELL_SIZE) == snake_head:
                powerup.activate(snake_head, enemies)
                self.powerups.remove(powerup)
                return powerup.effect.__name__  # Return the effect name
        return None

    # Power-up Effects
    def speed_boost(self, player, enemies):
        player.speed *= 2
        print("Speed Boost Activated!")

    def shield(self, player, enemies):
        player.activate_shield(duration=200)
        print("Shield Activated!")

    def power_boost(self, player, enemies):
        player.attack_power += 1
        print("Power Boost Activated!")

    def midas_touch(self, player, enemies):
        player.double_points = True
        print("Midas Touch Activated!")

    def freeze_enemies(self, player, enemies):
        for enemy in enemies:
            enemy.frozen = True
            enemy.freeze_timer = 200  # Example duration
        print("Enemies Frozen!")

    def growth_boost(self, player, enemies):
        for _ in range(3):  # Add three segments
            player.grow = True
            player.move()
        print("Growth Boost Activated!")

    def teleportation(self, player, enemies):
        teleport_effect = TeleportationEffect(
            POWERUP_SPRITES["teleportation_start"],
            POWERUP_SPRITES["teleportation_end"],
            CELL_SIZE
        )
        teleport_effect.start_teleport()
        print("Teleportation Activated!")
