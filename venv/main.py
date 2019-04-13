from tkinter import *

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

    def __init__(self, world):
        self.pdWorld = world

    def new_window(self, title):
        window = Toplevel(self.main_window)
        window.title(title)

        if title == "PD-World":
            self.pd_world_window = window
            self.create_labels()
        if title == "Q-Table":
            self.qTable_window = window
            for r in range(1,6) :
                for c in range(1,6):
                    Label(self.qTable_window, text = '0', borderwidth = 12).grid(row=r,column=c)

    def create_labels(self):
        for i in self.pdWorld.cells:
            if i.type == CellType.PICKUP:
                Label(self.pd_world_window, text='(%s,%s)' % i.position, borderwidth=12, fg="green").grid(
                    row=i.position[0], column=i.position[1])
            elif i.type == CellType.DROPOFF:
                Label(self.pd_world_window, text='(%s,%s)' % i.position, borderwidth=12, fg="blue").grid(
                    row=i.position[0], column=i.position[1])
            else:
                Label(self.pd_world_window, text='(%s,%s)' % i.position, borderwidth=12).grid(row=i.position[0],
                                                                                              column=i.position[1])

    def create_pdworld(self):
        self.view_world_button = Button(self.main_window, text='View World', pady=10, width=25, background='#4d88ff',
                                        command=lambda: self.new_window("PD-World"))
        square1 = Frame(self.main_window, bg="red")
        square1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W+E+N+S)

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
gui = GUI(world)
gui.create_pdworld()
gui.create_qTable()
gui.generate()