## File: main.py
import pygame
from config import TILESET, WIDTH, HEIGHT, CELL_SIZE, BLACK, FPS, SNAKE_SKINS, FONTS
from snake import Snake
from tiles import TileMap
from sounds import Sounds
from powerups import PowerUpManager
from maps import Maps
from gui import GUI
from effects import BloodSplatter
from powerups import TeleportationEffect
from utils import draw_text
import os

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load fonts
font_title = pygame.font.Font(FONTS["title"], 72)
font_subtitle = pygame.font.Font(FONTS["subtitle"], 48)
font_score = pygame.font.Font(FONTS["score"], 36)

# Load maps
maps = Maps()
selected_map_name = None
selected_snake_skin = None
selected_enemy_skin = None

# Blood splatter effects
blood_splatters = []
blood_sprite_sheet = "assets/sprites/blood_hit_01.png"  # Example sprite sheet path

# Initialize teleportation effect
teleport_effect = TeleportationEffect(
    "assets/sprites/teleporter_01.png",
    "assets/sprites/teleporter_hit.png",
    CELL_SIZE,
)

def select_map():
    """Display a map selection menu."""
    menu = GUI()
    map_names = maps.list_maps()
    selected_map = menu.show_options(map_names, "Select a Map")
    return selected_map

def select_snake_skin(title):
    """Display a snake skin selection menu."""
    menu = GUI()
    skin_names = list(SNAKE_SKINS.keys())
    selected_skin = menu.show_options(skin_names, title)
    return SNAKE_SKINS[selected_skin]

def main_menu():
    """Main menu interface."""
    menu = GUI()
    while True:
        screen.fill(BLACK)
        draw_text(screen, "Snake Rivals", font_title, (255, 255, 255), WIDTH // 2 - 200, 50)
        draw_text(screen, "Press Start to Begin", font_subtitle, (200, 200, 200), WIDTH // 2 - 150, 150)
        action = menu.main_menu(screen)
        if action == "Start Game":
            break
        elif action == "Settings":
            print("Settings menu not implemented yet!")
        elif action == "Exit":
            pygame.quit()
            exit()

        pygame.display.flip()
        clock.tick(FPS)

# Create objects
tile_map = None
player = None
enemy = None
sounds = Sounds()
powerup_manager = PowerUpManager(spawn_count=3)

def main():
    global selected_map_name, selected_snake_skin, selected_enemy_skin, tile_map, player, enemy, blood_splatters

    # Show main menu
    main_menu()

    # Select map and skins using GUI
    selected_map_name = select_map()
    selected_snake_skin = select_snake_skin("Select Player Snake Skin")
    selected_enemy_skin = select_snake_skin("Select Enemy Snake Skin")
    selected_map_data = maps.get_map(selected_map_name)

    # Initialize game objects
    tile_map = TileMap(selected_map_data, TILESET)
    player = Snake(selected_snake_skin, WIDTH // 2, HEIGHT // 2)
    enemy = Snake(selected_enemy_skin, WIDTH // 4, HEIGHT // 4, is_enemy=True)

    running = True
    sounds.play_menu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update snakes
        player.move()
        enemy.move()  # Assuming enemy AI logic is implemented
        player.update_shield()  # Update shield visuals and state

        # Check collisions for powerups
        if powerup_manager.check_collisions(player.body[0]) == "teleportation":
            teleport_effect.start_teleport()

        # Handle teleportation animation
        if teleport_effect.animating:
            teleport_effect.update(screen, player.body[0][0], player.body[0][1])
        elif teleport_effect.teleport_done:
            player.body[0] = [WIDTH // 3, HEIGHT // 3]  # Example teleport location
            teleport_effect.teleport_done = False

        # Trigger blood effects when player or enemy takes damage
        if not player.alive:
            x, y = player.body[0]
            blood_splatters.append(BloodSplatter(x, y, blood_sprite_sheet, CELL_SIZE))

        if not enemy.alive:
            x, y = enemy.body[0]
            blood_splatters.append(BloodSplatter(x, y, blood_sprite_sheet, CELL_SIZE))

        # Update blood splatters
        for splatter in blood_splatters:
            splatter.update()

        # Remove inactive blood splatters
        blood_splatters = [s for s in blood_splatters if s.active]

        # Draw everything
        screen.fill(BLACK)
        tile_map.draw(screen)
        powerup_manager.draw(screen)
        player.draw(screen)
        enemy.draw(screen)

        # Draw blood splatters
        for splatter in blood_splatters:
            splatter.draw(screen)

        # Draw score or other UI
        draw_text(screen, "Score: 0", font_score, (255, 255, 255), 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

    sounds.play_game_over()
    pygame.quit()

if __name__ == "__main__":
    main()
