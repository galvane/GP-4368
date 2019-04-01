from tkinter import *

class GUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Reinforcement Learning")
        self.main_window.geometry("500x200")

    def new_window(self, title):
        window = Toplevel(self.main_window)
        window.title("PD-World")
        window.geometry("500x500")

    def createPDWorld(self):
        self.view_world_button = Button(self.main_window, text ='View World', pady = 10 ,width = 25, background = '#4d88ff', command = lambda:self.new_window("PD-World"))

    def generate(self):
        # add to main window
        self.view_world_button.pack()
        self.main_window.mainloop()

gui = GUI()
gui.createPDWorld()
gui.generate()