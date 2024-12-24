import pygame
from config import WHITE, BLACK, WIDTH, HEIGHT

class GUI:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)

    def draw_essence(self, surface, essence, win_essence):
        text = self.font.render(f"Essence: {essence}/{win_essence}", True, WHITE)
        surface.blit(text, (10, 10))

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

    def draw_button(self, surface, text, rect, hover=False):
        """Draws a button with optional hover effect."""
        color = WHITE if hover else BLACK
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, WHITE, rect, 2)  # Border
        font = pygame.font.SysFont(None, 36)
        label = font.render(text, True, WHITE if hover else BLACK)
        label_rect = label.get_rect(center=rect.center)
        surface.blit(label, label_rect)

    def main_menu(self, surface):
        """Main menu interface."""
        menu_font = pygame.font.SysFont(None, 60)
        title = menu_font.render("SNAKE RIVALS", True, WHITE)
        surface.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        # Button configurations
        buttons = {
            "Start Game": pygame.Rect(WIDTH // 2 - 100, 200, 200, 50),
            "Settings": pygame.Rect(WIDTH // 2 - 100, 300, 200, 50),
            "Exit": pygame.Rect(WIDTH // 2 - 100, 400, 200, 50),
        }

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        for text, rect in buttons.items():
            hover = rect.collidepoint(mouse_pos)
            self.draw_button(surface, text, rect, hover)

            # Check for clicks
            if hover and mouse_click:
                return text  # Return the button text to determine action

        return None
