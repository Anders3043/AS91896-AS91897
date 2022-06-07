# This program is for Julie to keep track of the item she hired out to people

from tkinter import *


# Making entries
def entries():
    global first_name, last_name, item, amount, recpit
    Label().grid(column=1, row=1)
    first_name = Entry().grid(column=2, row=2)
    Label(font='bold', text="First name").grid(column=1, row=2)
    Label().grid(column=1, row=3)
    last_name = Entry().grid(column=2,row=4)
    Label(font='bold', text="Last name").grid(column=1, row=4)
    Label().grid(column=1, row=5)
    item = Entry().grid(column=2, row=6)
    Label(font='bold', text="Item hired").grid(column=1, row=6)
    Label().grid(column=1, row=7)
    amount = Entry().grid(column=2, row=8)
    Label(font='bold', text="Amount of item hired").grid(column=1, row=8)
    Label().grid(column=1, row=9)

def quit():
    main_window.destroy()


def buttons():
    Button(main_window, text="Quit", command=quit).grid(column=1, row=0)

# Running the window
main_window = Tk()
entries()
buttons()
main_window.geometry("800x1000")
main_window.mainloop()
