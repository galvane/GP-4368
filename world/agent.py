from tkinter import *
from enum import Enum

class OperatorType(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Operator:
    direction = None
    isApplicable = True
    def __init__(self,  type):
        self.direction = type

    def setApplicability(self, isApplicable):
        self.isApplicable = isApplicable

    def getApplicability(self, operator):
        return operator.isApplicable

class Agent:
    world = None
    position = None
    img = None
    operators = []

    def __init__(self, world):
        self.img = PhotoImage(file="frog.png")
        self.img = self.img.subsample(15)
        self.world = world
        self.position = world.startCell

        op = [Operator(OperatorType.NORTH),
              Operator(OperatorType.EAST),
              Operator(OperatorType.SOUTH),
              Operator(OperatorType.WEST)]
        self.operators.append(op)