# This program is for Julie to keep track of the item she hired out to people

from tkinter import *


# Making entries
def entries():
    global first_name, last_name, item, amount, receipt
    Label().grid(column=1, row=1)
    first_name = Entry(main_window)
    first_name.grid(column=2, row=2)
    Label(font='bold', text="First name").grid(column=1, row=2)
    Label().grid(column=1, row=3)
    last_name = Entry(main_window)
    last_name.grid(column=2, row=4)
    Label(font='bold', text="Last name").grid(column=1, row=4)
    Label().grid(column=1, row=5)
    item = Entry(main_window)
    item.grid(column=2, row=6)
    Label(font='bold', text="Item hired").grid(column=1, row=6)
    Label().grid(column=1, row=7)
    amount = Entry(main_window)
    amount.grid(column=2, row=8)
    Label(font='bold', text="Amount of item hired").grid(column=1, row=8)
    Label().grid(column=1, row=9)
    Label().grid(column=5,row=0)


def quit_program():
    main_window.destroy()


def buttons():
    Button(main_window, text="Quit", command=quit_program).grid(column=1, row=0)
    Button(main_window, text="Append details", command=append).grid(column=7, row=2)


def append():
    global first_name, last_name, item, amount, receipt
    total_entries = 0
    if len(first_name.get()) == 0:
        Label(text="Please do not leave this blank", fg='red').grid(column=3, row=2)
    else:
        total_entries += 1
    if len(last_name.get()) == 0:
        Label(text="Please do not leave this blank", fg='red').grid(column=3, row=4)
    else:
        total_entries += 1
    if len(item.get()) == 0:
        Label(text="Please do not leave this blank", fg='red').grid(column=3, row=6)
    else:
        total_entries += 1
    if len(amount.get()) == 0:
        Label(text="Please do not leave this blank", fg='red').grid(column=3, row=8)
    else:
        total_entries += 1



# Running the window
main_window = Tk()
entries()
buttons()
main_window.geometry("500x400")
main_window.mainloop()
