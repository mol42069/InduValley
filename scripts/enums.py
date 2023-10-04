from enum import Enum

class SheetPos(Enum):

    Empty = (0, 0)

class Cor(Enum):

    X = 0
    Y = 1

class CropTimer(Enum):

    Wheat = 4
    Blueberry = 6

class Direction(Enum):

    UP = 3
    DOWN = 0
    RIGHT = 2
    LEFT = 1

