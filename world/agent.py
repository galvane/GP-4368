from tkinter import *
class Agent:
    world = None
    position = None
    img = None
    def __init__(self, world):
        self.img = PhotoImage(file="frog.png")
        self.img = self.img.subsample(15)
        self.world = world
        self.position = world.startCell
