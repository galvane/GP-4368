from tkinter import *

from world.agent import Agent, ActionType
from world.cell import CellType
from world.pdworld import PDWorld


class GUI:
    main_window = Tk()
    main_window.title("Reinforcement Learning")
    main_window.geometry("250x500")
    view_world_button = None
    pd_world_window = None
    qTable_window = None
    pdWorld = None
    labels = []
    agent = None

    def __init__(self, world, agent):
        self.pdWorld = world
        self.agent = agent

    def new_window(self, title):
        window = Toplevel(self.main_window)
        window.title(title)
        if title == "PD-World":
            self.pd_world_window = window
            self.pd_world_window.grid_columnconfigure(0, weight=0)
            self.pd_world_window.grid_columnconfigure(1, weight=1)
            self.pd_world_window.grid_columnconfigure(2, weight=1)
            self.pd_world_window.grid_columnconfigure(3, weight=1)
            self.pd_world_window.grid_columnconfigure(4, weight=1)
            self.pd_world_window.grid_columnconfigure(5, weight=1)
            self.pd_world_window.grid_rowconfigure(0, weight=0)
            self.pd_world_window.grid_rowconfigure(1, weight=1)
            self.pd_world_window.grid_rowconfigure(2, weight=1)
            self.pd_world_window.grid_rowconfigure(3, weight=1)
            self.pd_world_window.grid_rowconfigure(4, weight=1)
            self.pd_world_window.grid_rowconfigure(5, weight=1)
            self.pd_world_window.geometry("600x600")
            self.create_labels()
            self.addAgentToPDWorld()
        if title == "Q-Table":
            self.qTable_window = window
            for r in range(1,6) :
                for c in range(1,6):
                    Label(self.qTable_window, text = '0', borderwidth = 12).grid(row=r,column=c)

    def create_labels(self):
        for i in self.pdWorld.cells:
            if i.type == CellType.PICKUP:
                label = Label(self.pd_world_window, text='(%s,%s)' % i.position, bd=1, fg="white", relief=GROOVE, background="blue", font=("Helvetica", 12))
                label.grid(row=i.position[0], column=i.position[1], sticky='NSEW')
                self.labels.append(label)
            elif i.type == CellType.DROPOFF:
                label = Label(self.pd_world_window, text='(%s,%s)' % i.position, bd=1, fg="white", relief=GROOVE, background="green", font=("Helvetica", 12))
                label.grid(row=i.position[0], column=i.position[1], sticky='NSEW')
                self.labels.append(label)
            else:
                label = Label(self.pd_world_window, text='(%s,%s)' % i.position, bd=1, fg = "white", highlightthickness = 50, relief=GROOVE, background="black", font=("Helvetica", 12))
                label.grid(row=i.position[0],column=i.position[1], sticky='NSEW')
                self.labels.append(label)

    def addAgentToPDWorld(self):
        for l in self.labels:
            if l.cget("text") == "("+','.join(map(str, agent.agentPosition.position))+ ")":
                l.config(image=self.agent.img)

    def create_pdworld(self):
        self.view_world_button = Button(self.main_window, text='View World', pady=10, width=25, background='#4d88ff',
                                        command=lambda: self.new_window("PD-World"))
        square1 = Frame(self.main_window, bg="red")
        square1.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E)

        self.view_world_button.grid()
        self.view_world_button.place(relx=0.5, rely=0.1, anchor=CENTER)

    def create_qTable(self):
        self.view_qTable_button = Button(self.main_window, text='View Q-Table', pady=10, width=25, background='#4d88ff',
                                         command=lambda: self.new_window("Q-Table"))

        self.view_qTable_button.grid()
        self.view_qTable_button.place(relx=0.5, rely=.25, anchor=S)

    def generate(self):
        self.main_window.mainloop()

world = PDWorld()
agent = Agent(world)
agent.move(ActionType.SOUTH)
gui = GUI(world, agent)
gui.create_pdworld()
gui.create_qTable()
gui.generate()

