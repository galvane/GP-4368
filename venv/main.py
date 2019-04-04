from tkinter import *

class GUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Reinforcement Learning")
        self.main_window.geometry("250x500")
        self.view_world_button = None
        self.pd_world_window = None

    def new_window(self, title):
        window = Toplevel(self.main_window)
        window.title(title)

        if title == "PD-World":
            self.pd_world_window = window
            for r in range(1,6):
                for c in range(1,6):
                    Label(self.pd_world_window, text = '(%s,%s)'%(r,c), borderwidth=12 ).grid(row=r,column=c)


    def create_pdworld(self):
        self.view_world_button = Button(self.main_window, text='View World', pady=10, width=25, background='#4d88ff',
                                        command=lambda: self.new_window("PD-World"))

        self.view_world_button.grid()
        self.view_world_button.place(relx=0.5, rely=0.1, anchor=CENTER)


    def create_qTable(self):
        self.view_qTable_button = Button(self.main_window, text='View Q-Table', pady=10, width=25, background='#4d88ff',
                                         command=lambda: self.new_window("Q-Table"))

        self.view_qTable_button.grid()
        self.view_qTable_button.place(relx=0.5, rely=.25, anchor=S)

    def generate(self):
        self.main_window.mainloop()

gui = GUI()
gui.create_pdworld()
gui.create_qTable()
gui.generate()