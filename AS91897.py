# This program is for Julie to keep track of the item she hired out to people

from tkinter import *

def buttons():
    global first_name, last_name, item, amount, recpit
    Label().grid(column=1, row=1)
    first_name = Entry().grid(column=2, row=2)
    Label(text="First name").grid(column=1, row=2)
    Label().grid(column=1, row=3)
    last_name = Entry().grid(column=2,row=4)
    Label(text="Last name").grid(column=1, row=4)
    Label().grid(column=1, row=5)
    item = Entry().grid(column=2, row=6)
    Label(text="Item hired").grid(column=1, row=6)
    Label().grid(column=1, row=7)
    amount = Entry().grid(column=2, row=8)
    Label(text="Amount of item hired").grid(column=1, row=8)
    Label().grid(column=1, row=9)


root = Tk()
buttons()
root.geometry("800x1000")
root.mainloop()
