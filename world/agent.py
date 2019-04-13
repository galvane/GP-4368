from tkinter import *
from enum import Enum
import collections

from world.cell import Cell, CellType


class ActionType(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    PICKUP = 5
    DROPOFF = 6

class Action:
    actionType = None
    qValue = 0
    def __init__(self,  type):
        self.actionType = type

    def setApplicability(self, isApplicable):
        self.isApplicable = isApplicable

    def getApplicability(self, agent):
        return agent.move(self.actionType)

class Agent:
    world = None
    agentPosition = None
    img = None
    operators = []

    def __init__(self, world):
        self.img = PhotoImage(file="frog.png")
        self.img = self.img.subsample(15)
        self.world = world
        self.agentPosition = world.startCell

        op = [Action(ActionType.NORTH),
              Action(ActionType.EAST),
              Action(ActionType.SOUTH),
              Action(ActionType.WEST)]
        self.operators.append(op)

    """PD-WORLD FOR SOME REASON HAS X AND Y COORDINATES FLIPPED"""
    def move(self, action_type):

        canMove = True
        x = self.agentPosition[0]
        y = self.agentPosition[1]

        oldPosition = self.agentPosition
        if action_type == ActionType.NORTH:
            self.newx = x - 1
            self.agentPosition = self.validateMove(self.newx, y)
        elif action_type == ActionType.EAST:
            self.newy = y + 1
            self.agentPosition = self.validateMove(x, self.newy)
        elif action_type == ActionType.SOUTH:
            self.newx = x + 1
            self.agentPosition = self.validateMove(self.newx, y)
        elif action_type == ActionType.WEST:
            self.newy = y - 1
            self.agentPosition = self.validateMove(x, self.newy)
        elif action_type == ActionType.PICKUP:
            canMove = self.agentPosition.blocks > 0
        elif action_type == ActionType.DROPOFF:
            canMove = self.agentPosition.blocks < 5
        else:
            print("[WARNING]: " + "Invalid operator!")
            canMove = False


        print("applied action: " ,end ="")
        print(action_type, end ="")
        print(" ==> agent moved from " + "(" ,oldPosition, ")" + " to " + "(" ,self.agentPosition,")")

        return canMove


    def validateMove(self, x, y):
        newx = x
        newy = y
        if self.validateNewX(x) and self.validateNewY(y):
            newCell = self.world.getCell(newx, newy)
            self.agentPosition = newCell
            return self.agentPosition
        elif self.validateNewX(x) and not self.validateNewY(y):
            newCell = self.world.getCell(newx, y)
            self.agentPosition = newCell
            return self.agentPosition
        elif not self.validateNewX(x) and self.validateNewY(y):
            newCell = self.world.getCell(x, newy)
            self.agentPosition = newCell
            return self.agentPosition
        else:
            newCell = self.world.getCell(x, y)
            self.agentPosition = newCell
            return self.agentPosition

    def validateNewX(self, x):
        if x > 5 or x < 0:
            return False
        return True
    def validateNewY(self, y):
        if y > 5 or y < 0:
            return False
        return True