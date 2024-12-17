## File: main.py
import pygame
import sys
from snake import Snake
from food import Food
from obstacles import Obstacle
from sounds import Sounds
from gui import GUI
from events import Events
from save_data import SaveData
from settings import Settings
from config import BLACK, GREEN, RED

pygame.init()
clock = pygame.time.Clock()

# Settings
settings = Settings()
window_size = settings.window_size
FPS = settings.fps
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake Rivals")

# Initialize other components
gui = GUI()
sounds = Sounds()
events = Events()
save_data = SaveData()


def main():
    player = Snake(settings.player_color, window_size[0] // 2, window_size[1] // 2)
    enemies = [Snake(settings.enemy_color, 100, 100, is_enemy=True)]
    food = Food()
    obstacles = Obstacle(count=5)
    essence = 0
    WIN_ESSENCE = 10

    paused = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_data.save_data(essence)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if paused and event.key == pygame.K_s:
                    show_settings_menu()

        if paused:
            gui.draw_pause_menu(screen, save_data.get_highscore())
            pygame.display.flip()
            continue

        screen.fill(BLACK)

        # Movement and Game Logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.direction != (0, 1):
            player.direction = (0, -1)
        if keys[pygame.K_DOWN] and player.direction != (0, -1):
            player.direction = (0, 1)
        if keys[pygame.K_LEFT] and player.direction != (1, 0):
            player.direction = (-1, 0)
        if keys[pygame.K_RIGHT] and player.direction != (-1, 0):
            player.direction = (1, 0)

        player.move()
        player.check_collision([player] + enemies, obstacles.get_positions())

        for enemy in enemies:
            enemy.move()
            enemy.check_collision([player] + enemies, obstacles.get_positions())

        if player.body[0] == food.position:
            sounds.play_food()
            player.grow = True
            essence += 1
            food = Food()
        
        player.draw(screen)
        food.draw(screen)
        obstacles.draw(screen)
        gui.draw_essence(screen, essence, WIN_ESSENCE)

        if essence >= WIN_ESSENCE:
            sounds.play_game_over()
            save_data.save_data(essence)
            print("You Win!")
            running = False

        pygame.display.flip()
        clock.tick(settings.fps)


def show_settings_menu():
    in_settings = True
    while in_settings:
        screen.fill(BLACK)
        settings.show_menu(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_settings = False

if __name__ == "__main__":
    main()
