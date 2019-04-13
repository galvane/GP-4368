from tkinter import *
from enum import Enum
import collections


class OperatorType(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Operator:
    direction = None
    isApplicable = True
    qValue = 0
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

    """PD-WORLD FOR SOME REASON HAS X AND Y COORDINATES FLIPPED"""
    def move(self, direction):

        x = self.position[0]
        y = self.position[1]

        oldPosition = self.position
        if direction == OperatorType.NORTH:
            self.newx = x - 1
            self.position = self.validatePosition(self.newx, y)
        elif direction == OperatorType.EAST:
            self.newy = y + 1
            self.position = self.validatePosition(x, self.newy)
        elif direction == OperatorType.SOUTH:
            self.newx = x + 1
            self.position = self.validatePosition(self.newx, y)
        elif direction == OperatorType.WEST:
            self.newy = y - 1
            self.position = self.validatePosition(x, self.newy)
        else:
            print("[WARNING]: " + "Invalid operator!")


        print("applied action: " ,end ="")
        print(direction, end = "")
        print(" ==> agent moved from " + "("+','.join(map(str, oldPosition))+")" + " to " + "("+','.join(map(str, self.position))+")")


    def validatePosition(self, x, y):
        point = collections.namedtuple('point', ['x', 'y'])
        newx = x
        newy = y
        if self.validateNewX(x) and self.validateNewY(y):
            self.position = point(newx, newy)
            return self.position
        elif self.validateNewX(x) and not self.validateNewY(y):
            self.position = point(newx, y)
            return self.position
        elif not self.validateNewX(x) and self.validateNewY(y):
            self.position = point(x, newy)
            return self.position
        else:
            self.position = point(x, newy)
            return self.position

    def validateNewX(self, x):
        if x > 5 or x < 0:
            return False
        return True
    def validateNewY(self, y):
        if y > 5 or y < 0:
            return False
        return True