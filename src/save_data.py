## File: save_data.py
import json

class SaveData:
    def __init__(self, file="savegame.json"):
        self.file = file
        self.data = {"highscore": 0}
        self.load_data()

    def save_data(self, score):
        if score > self.data["highscore"]:
            self.data["highscore"] = score
            with open(self.file, "w") as f:
                json.dump(self.data, f)

    def load_data(self):
        try:
            with open(self.file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"highscore": 0}

    def get_highscore(self):
        return self.data["highscore"]
