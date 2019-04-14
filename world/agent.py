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
        return agent.validateActionType(self.actionType)

class Agent:
    world = None
    agentPosition = None
    img = None
    operators = []

    def __init__(self, world):
        self.img = PhotoImage(file="robot.png")
        self.img = self.img.subsample(13)
        self.world = world
        self.agentPosition = world.startCell

        op = [Action(ActionType.PICKUP),
              Action(ActionType.DROPOFF),
              Action(ActionType.NORTH),
              Action(ActionType.EAST),
              Action(ActionType.SOUTH),
              Action(ActionType.WEST)]
        self.operators.extend(op)



    def validateActionType(self, action_type):
        x = self.agentPosition.position[0]
        y = self.agentPosition.position[1]

        oldState = self.agentPosition
        if action_type == ActionType.NORTH:
            self.newx = x - 1
            if not self.validateMove(self.newx, y):
                return False

        elif action_type == ActionType.EAST:
            self.newy = y + 1
            if not self.validateMove(x, self.newy):
                return False


        elif action_type == ActionType.SOUTH:
            self.newx = x + 1
            if not self.validateMove(self.newx, y):
                return False


        elif action_type == ActionType.WEST:
            self.newy = y - 1
            if not self.validateMove(x, self.newy):
                return False

        elif action_type == ActionType.PICKUP:
            return self.agentPosition.blocks > 0 and self.agentPosition.type == CellType.PICKUP

        elif action_type == ActionType.DROPOFF:
            return self.agentPosition.blocks < 5 and self.agentPosition.type == CellType.DROPOFF

        return True

    """PD-WORLD FOR SOME REASON HAS X AND Y COORDINATES FLIPPED"""
    def move(self, action_type):
        x = self.agentPosition.position[0]
        y = self.agentPosition.position[1]

        oldState = self.agentPosition
        if action_type == ActionType.NORTH:
            self.newx = x - 1
            if self.validateActionType(action_type):
                self.agentPosition = self.world.getCell(self.newx, y)

        elif action_type == ActionType.EAST:
            self.newy = y + 1
            if self.validateMove(x, self.newy):
                self.agentPosition = self.world.getCell(x, self.newy)

        elif action_type == ActionType.SOUTH:
            self.newx = x + 1
            if self.validateMove(self.newx, y):
                self.agentPosition = self.world.getCell(self.newx, y)

        elif action_type == ActionType.WEST:
            self.newy = y - 1
            if self.validateMove(x, self.newy):
                self.agentPosition = self.world.getCell(x, self.newy)

        elif action_type == ActionType.PICKUP:
            self.agentPosition.blocks = self.agentPosition.blocks - 1

        elif action_type == ActionType.DROPOFF:
            self.agentPosition.block = self.agentPosition.blocks + 1

        else:
            print("[WARNING]: " + "Invalid operator!")

        # if successful:
        #     print("applied action: ", end ="")
        #     print(action_type, end ="")
        #     print(" ==> agent moved from " + "(" ,oldState.position, ")" + " to " + "(" ,self.agentPosition.position,")")
        # else:
        #     print("agent attempted to move ", end="")
        #     print(action_type, end="")


    def validateMove(self, x, y):
        if self.validateNewX(x) and self.validateNewY(y):
            return True
        return False

    def validateNewX(self, x):
        if x > 5 or x < 1:
            return False
        return True
    def validateNewY(self, y):
        if y > 5 or y < 1:
            return False
        return True