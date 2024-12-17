## File: main.py
import pygame
from config import TILESET, WIDTH, HEIGHT, CELL_SIZE, BLACK, FPS
from snake import Snake
from tiles import TileMap

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Updated map data using new tiles
MAP_DATA = [
    [0, 0, 1, 1, 0, 2, 2],
    [0, 2, 3, 4, 0, 0, 3],
    [1, 5, 0, 6, 7, 7, 4],
    [1, 0, 3, 4, 5, 6, 0],
    [2, 3, 3, 4, 4, 5, 0]
]

# Create objects
tile_map = TileMap(MAP_DATA, TILESET)
player = Snake((255, 0, 0), WIDTH // 2, HEIGHT // 2)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background and tiles
        screen.fill(BLACK)
        tile_map.draw(screen)

        # Update and draw the player
        player.move()
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
