from tkinter import *

main_window = Tk()

main_window.title("Reinforcement Learning")
main_window.geometry("500x200")

def new_window():
    window = Toplevel(main_window)
    window.title("PD World")
    window.geometry("500x500")

view_world_button = Button(main_window, text ='View World', pady = 10 ,width = 25, background = '#4d88ff', command = new_window)
close_button = Button(main_window, text = 'Close', pady = 20, width = 25, command = main_window.destroy)

# add to main window
view_world_button.pack()
close_button.pack()

main_window.mainloop()