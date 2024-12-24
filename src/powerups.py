import pygame
import random
import os
from config import CELL_SIZE
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
        base_path = os.path.dirname(__file__)
        dematerialize_path = os.path.join(base_path, "../", dematerialize_sprites)
        materialize_path = os.path.join(base_path, "../", materialize_sprites)

        self.dematerialize_frames = load_animation_frames(dematerialize_path, cell_size, cell_size)
        self.materialize_frames = load_animation_frames(materialize_path, cell_size, cell_size)
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
        self.images = {
            "speed": "assets/sprites/power_speed.png",
            "shield": "assets/sprites/power_shield.png",
            "power": "assets/sprites/power_power.png",
            "midas": "assets/sprites/power_midas.png",
            "freeze": "assets/sprites/power_freeze.png",
            "growth": "assets/sprites/power_growth.png",
            "teleportation": "assets/sprites/teleporter_01.png"
        }

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
                return True
        return False

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
            "assets/sprites/teleporter_hit.png",
            "assets/sprites/teleporter_01.png",
            CELL_SIZE
        )
        teleport_effect.start_teleport()
        print("Teleportation Activated!")
