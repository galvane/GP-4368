from enum import Enum
from tkinter import PhotoImage


class CellType(Enum):
    DROPOFF = 0
    PICKUP = 1
    REGULAR = 2


class Cell:
    def __init__(self, type, coordinates):
        self.type = type
        self.hasAgent = False
        self.blocks = 5 if (self.type == CellType.PICKUP) else 0
        self.position = coordinates
        self.qValue = 0
        self.reward = None

        if type == CellType.PICKUP or type == CellType.DROPOFF:
            self.reward = 13
        else:
            self.reward = -1


    def updateQValue(self, newQValue):
        self.qValue = newQValue
