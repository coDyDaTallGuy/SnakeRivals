## File: settings.py
import pygame
from config import WIDTH, HEIGHT, FPS, WHITE

DEFAULT_WINDOW_SIZE = (WIDTH, HEIGHT)
DEFAULT_FPS = FPS
DEFAULT_SNAKE_SPEED = 5
DEFAULT_SNAKE_COLOR = (0, 255, 0)  # Green
DEFAULT_ENEMY_COLOR = (255, 0, 0)  # Red

class Settings:
    def __init__(self):
        self.window_size = DEFAULT_WINDOW_SIZE
        self.fps = DEFAULT_FPS
        self.snake_speed = DEFAULT_SNAKE_SPEED
        self.player_color = DEFAULT_SNAKE_COLOR
        self.enemy_color = DEFAULT_ENEMY_COLOR

    def show_menu(self, surface):
        settings_font = pygame.font.SysFont(None, 36)
        menu_items = [
            "Settings:",
            f"1. Window Size: {self.window_size[0]}x{self.window_size[1]}",
            f"2. FPS: {self.fps}",
            f"3. Snake Speed: {self.snake_speed}",
            f"4. Player Color: {self.player_color}",
            f"5. Enemy Color: {self.enemy_color}",
            "Press ESC to return."
        ]
        y = 150
        for item in menu_items:
            text = settings_font.render(item, True, WHITE)
            surface.blit(text, (200, y))
            y += 40

    def update_setting(self, option, value):
        if option == 1:
            self.window_size = value
        elif option == 2:
            self.fps = value
        elif option == 3:
            self.snake_speed = value
        elif option == 4:
            self.player_color = value
        elif option == 5:
            self.enemy_color = value
