## File: maps.py

from config import WIDTH, HEIGHT, CELL_SIZE

class Maps:
    def __init__(self):
        self.maps = {
            "Sssandstorm": [
                [0, 4, 4, 4, 0],
                [4, 4, 0, 4, 4],
                [4, 0, 0, 0, 4],
                [4, 4, 0, 4, 4],
                [0, 4, 4, 4, 0],
            ],
            "Grasssss Plains": [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            "Snakes on Ice": [
                [6, 6, 6, 6, 6],
                [6, 0, 0, 0, 6],
                [6, 0, 6, 0, 6],
                [6, 0, 0, 0, 6],
                [6, 6, 6, 6, 6],
            ],
            "Ssscorched Earth": [
                [5, 5, 5, 5, 5],
                [5, 0, 0, 0, 5],
                [5, 0, 5, 0, 5],
                [5, 0, 0, 0, 5],
                [5, 5, 5, 5, 5],
            ],
            "Bricksss and Mortar": [
                [7, 7, 7, 7, 7],
                [7, 0, 0, 0, 7],
                [7, 0, 7, 0, 7],
                [7, 0, 0, 0, 7],
                [7, 7, 7, 7, 7],
            ],
            "Rocky Roadsss": [
                [3, 3, 3, 3, 3],
                [3, 0, 0, 0, 3],
                [3, 0, 3, 0, 3],
                [3, 0, 0, 0, 3],
                [3, 3, 3, 3, 3],
            ],
            "Watery Grave": [
                [2, 2, 2, 2, 2],
                [2, 0, 0, 0, 2],
                [2, 0, 2, 0, 2],
                [2, 0, 0, 0, 2],
                [2, 2, 2, 2, 2],
            ],
            "Dirtsss Delight": [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            "Grassy Oasis": [
                [0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0],
                [0, 2, 2, 2, 0],
                [0, 0, 2, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            "Randomsss": [
                [4, 0, 2, 1, 3],
                [5, 7, 6, 1, 2],
                [3, 2, 0, 7, 4],
                [6, 1, 4, 5, 0],
                [2, 3, 1, 6, 5],
            ],
        }

    def get_map(self, name):
        base_map = self.maps.get(name, None)
        if base_map is None:
            return None

        # Calculate the number of cells needed to fill the window
        rows = HEIGHT // CELL_SIZE
        cols = WIDTH // CELL_SIZE

        # Create a new map with the required size
        new_map = [[0 for _ in range(cols)] for _ in range(rows)]

        # Fill the new map with the base map pattern
        for i in range(rows):
            for j in range(cols):
                new_map[i][j] = base_map[i % len(base_map)][j % len(base_map[0])]

        return new_map

    def list_maps(self):
        return list(self.maps.keys())
