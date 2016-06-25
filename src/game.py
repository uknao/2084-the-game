import json


class Level:

  def __init__(self, level_file):
    with open(level_file, "r") as f:
      level_data = json.loads(f.read())
      print level_data

class Game:

  def __init__(self):
    self.current_level = Level("level1.json")

  def start(self):
    self.current_level.play()  