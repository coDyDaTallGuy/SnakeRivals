## File: levels.py
class Levels:
    def __init__(self):
        self.levels = [
            {"obstacles": 5, "powerups": 1},
            {"obstacles": 10, "powerups": 2},
            {"obstacles": 15, "powerups": 3},
        ]

    def get_level(self, level_num):
        if level_num < len(self.levels):
            return self.levels[level_num]
        return self.levels[-1]
