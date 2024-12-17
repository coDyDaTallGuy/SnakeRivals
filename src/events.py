## File: events.py
class Events:
    def __init__(self):
        self.ticks = 0

    def update_ticks(self):
        self.ticks += 1

    def spawn_powerup(self):
        # Spawn powerups every 500 ticks
        return self.ticks % 500 == 0
