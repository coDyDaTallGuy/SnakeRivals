## File: gui.py
import pygame
from config import WHITE

class GUI:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)

    def draw_essence(self, surface, essence, win_essence):
        text = self.font.render(f"Essence: {essence}/{win_essence}", True, WHITE)
        surface.blit(text, (10, 10))

    def draw_menu(self, surface):
        menu_font = pygame.font.SysFont(None, 60)
        text = menu_font.render("SNAKE RIVALS", True, WHITE)
        surface.blit(text, (200, 250))

    def draw_pause_menu(self, surface, highscore):
        pause_font = pygame.font.SysFont(None, 50)
        text1 = pause_font.render("PAUSED", True, WHITE)
        text2 = self.font.render(f"High Score: {highscore}", True, WHITE)
        text3 = self.font.render("Press P to Resume", True, WHITE)
        text4 = self.font.render("Press S for Settings", True, WHITE)
        surface.blit(text1, (300, 200))
        surface.blit(text2, (300, 250))
        surface.blit(text3, (300, 300))
        surface.blit(text4, (300, 350))
