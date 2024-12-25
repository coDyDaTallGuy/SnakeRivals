import pygame
import sys

class SnakeController:
    def __init__(self):
        self.direction = pygame.Vector2(1, 0)  # Initial direction to the right
        self.snake_pos = pygame.Vector2(400, 300)  # Example initial snake position

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.direction != pygame.Vector2(0, 1):
                    self.direction = pygame.Vector2(0, -1)
                elif event.key == pygame.K_s and self.direction != pygame.Vector2(0, -1):
                    self.direction = pygame.Vector2(0, 1)
                elif event.key == pygame.K_a and self.direction != pygame.Vector2(1, 0):
                    self.direction = pygame.Vector2(-1, 0)
                elif event.key == pygame.K_d and self.direction != pygame.Vector2(-1, 0):
                    self.direction = pygame.Vector2(1, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    self.update_direction(mouse_pos)

    def update_direction(self, mouse_pos):
        # Update direction based on mouse position
        direction_vector = pygame.Vector2(mouse_pos) - self.snake_pos
        if abs(direction_vector.x) > abs(direction_vector.y):
            if direction_vector.x > 0 and self.direction != pygame.Vector2(-1, 0):
                self.direction = pygame.Vector2(1, 0)
            elif direction_vector.x < 0 and self.direction != pygame.Vector2(1, 0):
                self.direction = pygame.Vector2(-1, 0)
        else:
            if direction_vector.y > 0 and self.direction != pygame.Vector2(0, -1):
                self.direction = pygame.Vector2(0, 1)
            elif direction_vector.y < 0 and self.direction != pygame.Vector2(0, 1):
                self.direction = pygame.Vector2(0, -1)

    def get_direction(self):
        return self.direction

# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    controller = SnakeController()

    while True:
        controller.handle_events()
        direction = controller.get_direction()
        print(f"Current direction: {direction}")

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)