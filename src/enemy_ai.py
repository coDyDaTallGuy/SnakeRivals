## File: enemy_ai.py
import random
from snake import Snake
from config import WIDTH, HEIGHT, CELL_SIZE

class EnemyAI(Snake):
    def update_direction(self):
        # Simple AI: Randomly change direction sometimes
        if random.randint(0, 10) > 8:
            self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
