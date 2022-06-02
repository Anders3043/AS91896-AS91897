# This program is for Julie to keep track of the item she hired out to people

from tkinter import *

def buttons():
    global first_name, last_name, item, amount, recpit
    first_name = Entry().grid(column=2, row=2)
    Label(text="First name").grid(column=1, row=2)


root = Tk()
buttons()
root.geometry("800x1000")
root.mainloop()
