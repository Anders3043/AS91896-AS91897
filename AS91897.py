# This program is for Julie to keep track of the item she hired out to people

from tkinter import *
from tkinter import ttk


# Making entries
def entries():
    global first_name, last_name, item, amount, receipt, delete_entry
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
    delete_entry = Entry(main_window)
    Label().grid(column=4, row=7)
    delete_entry.grid(column=4, row=8)
    Label(font='bold', text="Receipt number here").grid(column=5, row=8)


# Function to quit the program
def quit_program():
    main_window.destroy()


# adding buttons
def buttons():
    Button(main_window, text="Quit", command=quit_program).grid(column=1, row=0)
    Button(main_window, text="Append details", command=append).grid(column=4, row=2)
    Label().grid(column=4, row=3)
    Button(main_window, text="Print details", command=print_list).grid(column=4, row=4)
    Label().grid(column=4, row=5)
    Button(main_window, text="Delete (Receipt number)", command=delete_list).grid(column=4, row=6)


# setting up for error message
first_name_error = 0
last_name_error = 0
item_error = 0
amount_error = 0
# set up for append and prints
hire_list = []
count = -1
total_entry = -1
pr = 0
twice = 0

def append():
    global first_name, last_name, item, amount, receipt, first_name_error, first_name_label, last_name_error, \
        last_name_label, item_error, item_label, amount_label, amount_error, total_entry, hire_list, twice, pr_labelgit
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
        first_name_label.grid_forget()
        first_name_error = 0
    else:
        first_name_error = 0
    if len(last_name.get()) == 0:
        last_name_label = Label(text="Please do not leave this blank", fg='red')
        last_name_label.grid(column=3, row=4)
        last_name_error += 1
    elif last_name_error > 0:
        last_name_label.grid_forget()
        last_name_error = 0
    else:
        last_name_error = 0
    if len(item.get()) == 0:
        item_label = Label(text="Please do not leave this blank", fg='red')
        item_label.grid(column=3, row=6)
        item_error += 1
    elif item_error > 0:
        item_label.grid_forget()
        item_error = 0
    else:
        item_error = 0
    if len(amount.get()) == 0:
        amount_label = Label(text="Please do not leave this blank", fg='red')
        amount_label.grid(column=3, row=8)
        amount_error += 1
    elif int(amount.get()) > 500 or int(amount.get()) < 1:
        amount_label = Label(text="Please make sure it's within 1-500", fg='red')
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
        amount_error = 0
    if len(first_name.get()) != 0 and len(last_name.get()) != 0 and amount_error == 0 and it_is == "True":
        hire_list.append([first_name.get(), last_name.get(), item.get(), amount.get()])
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        item.delete(0, 'end')
        amount.delete(0, 'end')
        total_entry += 1
    if twice == 1:
        pr_label = Label(main_window, text="Please press print twice")
        pr_label.grid(column=5, row=4)
        twice = 0

# Making print function
def print_list():
    global total_entry, count, L1, L2, L3, L4, L5, pr, twice, pr_label
    Label(main_window, font='bold', text="First name").grid(column=1, row=10)
    Label(main_window, font='bold', text="Last name").grid(column=2, row=10)
    Label(main_window, font='bold', text="Item hired").grid(column=3, row=10)
    Label(main_window, font='bold', text="Amount of item hired").grid(column=4, row=10)
    Label(main_window, font='bold', text="Receipt number").grid(column=5, row=10)

    if count < total_entry:
        L1 = Label(main_window, text=(hire_list[total_entry][0]))
        L1.grid(column=1, row=count + 12)
        L2 = Label(main_window, text=(hire_list[total_entry][1]))
        L2.grid(column=2, row=count + 12)
        L3 = Label(main_window, text=(hire_list[total_entry][2]))
        L3.grid(column=3, row=count + 12)
        L4 = Label(main_window, text=(hire_list[total_entry][3]))
        L4.grid(column=4, row=count + 12)
        L5 = Label(main_window, text=(count+2))
        L5.grid(column=5, row=count+12)
        count += 1
        pr += 1
    if pr == 2:
        pr_label.grid_forget()


def delete_list():
    global delete_entry, hire_list, total_entry, count, L1, L2, L3, L4, L5, count, twice, pr
    try:
        int(delete_entry.get())
        it_is2 = "True"
    except ValueError:
        it_is2 = "False"
    if it_is2 == "False":
        er = Label(main_window, text='Please make sure it is a number', fg='red')
        er.grid(column=6, row=8)
    else:
        deletes = int(delete_entry.get()) - 1
        del hire_list[int(deletes)]
        total_entry -= 1
        count -= 2
        pr = 0
        if count == -2:
            twice = 1
        delete_entry.delete(0, 'end')
        Label(main_window, text='                                                 ').grid(column=1, row=11)
        Label(main_window, text='                                                 ').grid(column=2, row=11)
        Label(main_window, text='                                                 ').grid(column=3, row=11)
        Label(main_window, text='                                                 ').grid(column=4, row=11)
        Label(main_window, text='                                                 ').grid(column=5, row=11)
        L1.grid_remove()
        L2.grid_remove()
        L3.grid_remove()
        L4.grid_remove()
        L5.grid_remove()
        print_list()


# Running the window
main_window = Tk()
entries()
buttons()
main_window.geometry("1000x600")
main_window.mainloop()
