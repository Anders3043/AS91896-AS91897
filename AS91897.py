# This program is for Julie to keep track of the item she hired out to people

from tkinter import *
from tkinter import ttk

total_entry = 0

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
    Label(text="                                                       ").grid(column=3, row=2)


def quit_program():
    main_window.destroy()


def buttons():
    Button(main_window, text="Quit", command=quit_program).grid(column=1, row=0)
    Button(main_window, text="Append details", command=append).grid(column=4, row=2)
    Label().grid(column=4, row=3)
    Button(main_window, text="Print details", command=print_list).grid(column=4, row=4)


# setting up for error message
first_name_error = 0
last_name_error = 0
item_error = 0
amount_error = 0
# set up for append and prints
hire_list = []
count = 0


def append():
    global first_name, last_name, item, amount, receipt, first_name_error, first_name_label, last_name_error, \
        last_name_label, item_error, item_label, amount_label, amount_error, total_entry, hire_list
    total_entries = 0
    try:
        int(amount.get())
        it_is = "True"
    except ValueError:
        it_is = "False"
    if len(first_name.get()) == 0:
        first_name_label = Label(main_window, text="Please do not leave this blank", fg='red')
        first_name_label.grid(column=3, row=2)
        first_name_error += 1
    elif first_name_error > 0:
        total_entries += 1
        first_name_label.grid_forget()
        first_name_error = 0
    else:
        total_entries += 1
        first_name_error = 0
    if len(last_name.get()) == 0:
        last_name_label = Label(text="Please do not leave this blank", fg='red')
        last_name_label.grid(column=3, row=4)
        last_name_error += 1
    elif last_name_error > 0:
        total_entries += 1
        last_name_label.grid_forget()
        last_name_error = 0
    else:
        total_entries += 1
        last_name_error = 0
    if len(item.get()) == 0:
        item_label = Label(text="Please do not leave this blank", fg='red')
        item_label.grid(column=3, row=6)
        item_error += 1
    elif item_error > 0:
        total_entries += 1
        item_label.grid_forget()
        item_error = 0
    else:
        total_entries += 1
        item_error = 0
    if len(amount.get()) == 0:
        amount_label = Label(text="Please do not leave this blank", fg='red')
        amount_label.grid(column=3, row=8)
        amount_error += 1
    elif amount_error > 0 and len(amount.get()) == 0:
        amount_label.grid_forget()
        amount_label = Label(text="Please do not leave this blank", fg='red')
        amount_label.grid(column=3, row=8)
        amount_error += 1
    elif it_is == "False":
        amount_label = Label(text="Please make sure this is a number", fg='red')
        amount_label.grid(column=3, row=8)
        amount_error += 1
    elif it_is == "False" and amount_error > 0:
        amount_label.grid_forget()
        amount_label = Label(text="Please make sure this is a number", fg='red')
        amount_label.grid(column=3, row=8)
        amount_error += 1
    elif amount_error > 0:
        amount_label.grid_forget()
        amount_error = 0
    else:
        total_entries += 1
        amount_error = 0
    if len(first_name.get()) != 0 and len(last_name.get()) != 0 and len(item.get()) != 0 and it_is == "True":
        hire_list.append(first_name.get())
        hire_list.append(last_name.get())
        hire_list.append(item.get())
        hire_list.append(amount.get())
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        item.delete(0, 'end')
        amount.delete(0, 'end')
        print(hire_list)
        total_entry += 1


# Making print function
def print_list():
    global total_entry, count
    count = 0
    Label(main_window, font='bold', text="First name").grid(column=1, row=10)
    Label(main_window, font='bold', text="Last name").grid(column=2, row=10)
    Label(main_window, font='bold', text="Item hired").grid(column=3, row=10)
    Label(main_window, font='bold', text="Amount of item hired").grid(column=4, row=10)

    if count < total_entry:
        Label(main_window, text=(hire_list[0])).grid(column=1, row=count + 11)
        Label(main_window, text=(hire_list[1])).grid(column=2, row=count + 11)
        Label(main_window, text=(hire_list[2])).grid(column=3, row=count + 11)
        Label(main_window, text=(hire_list[3])).grid(column=4, row=count + 11)
        count += 1


# Running the window
main_window = Tk()
entries()
buttons()
main_window.geometry("1000x600")
main_window.mainloop()
