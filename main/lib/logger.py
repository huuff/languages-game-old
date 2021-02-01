from enum import Enum

class Level(Enum):
    NONE = 0
    INFO = 1
    DEBUG = 2

class Logger():
    def __init__(self, level):
        self.level = level

    def log(self, message, level):
        if (self.level.value >= level.value):
            print(message)
