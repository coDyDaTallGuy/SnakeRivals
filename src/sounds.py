import pygame
from config import MENU_SOUND, GAME_OVER_SOUND, ATTACK_SOUND, FOOD_SOUND, POWERUP_SOUND

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        try:
            self.menu_sound = pygame.mixer.Sound(MENU_SOUND)
            self.game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
            self.attack_sound = pygame.mixer.Sound(ATTACK_SOUND)
            self.food_sound = pygame.mixer.Sound(FOOD_SOUND)
            self.powerup_sound = pygame.mixer.Sound(POWERUP_SOUND)
        except FileNotFoundError as e:
            print(f"Error loading sound file: {e}")
            self.menu_sound = self.game_over_sound = self.attack_sound = self.food_sound = self.powerup_sound = None

    def play_menu(self):
        if self.menu_sound:
            self.menu_sound.play()

    def play_game_over(self):
        if self.game_over_sound:
            self.game_over_sound.play()

    def play_attack(self):
        if self.attack_sound:
            self.attack_sound.play()

    def play_food(self):
        if self.food_sound:
            self.food_sound.play()

    def play_powerup(self):
        if self.powerup_sound:
            self.powerup_sound.play()
