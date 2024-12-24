## File: effects.py
import pygame
from utils import load_animation_frames

class BloodSplatter:
    def __init__(self, x, y, sprite_sheet, cell_size):
        self.position = (x, y)
        self.frames = load_animation_frames(sprite_sheet, cell_size, cell_size)
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_duration = 5  # Adjust for animation speed
        self.active = True

    def update(self):
        """Update the animation frame."""
        if not self.active:
            return

        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.active = False  # End animation

    def draw(self, surface):
        """Draw the current frame of the animation."""
        if self.active:
            frame = self.frames[self.current_frame]
            x, y = self.position
            surface.blit(frame, (x, y))
