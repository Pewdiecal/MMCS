import tkinter
from tkinter import ttk as tker
import os
import platform

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def add():
    print("add")


def remove():
    print("remove")


def confirm():
    print("confirm")


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Schedule Availability", font=label_font_screen)
select_day_label = tkinter.Label(top, text="Select Day")
select_time_label = tkinter.Label(top, text="Select Time (24Hrs format)")
dayList_box = tkinter.Listbox(top)
dayList_box.insert(1, "Monday")
dayList_box.insert(2, "Tuesday")
dayList_box.insert(3, "Wednesday")
dayList_box.insert(4, "Thursday")
dayList_box.insert(5, "Friday")
hrs_label = tkinter.Label(top, text="Hrs")
hrs_entry = tkinter.Entry(top, bd=5, width=5)
min_label = tkinter.Label(top, text="Mins")
min_entry = tkinter.Entry(top, bd=5, width=5)
hrs2_label = tkinter.Label(top, text="Hrs")
hrs2_entry = tkinter.Entry(top, bd=5, width=5)
mins2_label = tkinter.Label(top, text="Mins")
mins2_entry = tkinter.Entry(top, bd=5, width=5)
start_label = tkinter.Label(top, text="Start")
end_label = tkinter.Label(top, text="End")
to_label = tkinter.Label(top, text="To")
add_btn = tkinter.Button(top, text="Add Time", command=add, pady=4, padx=4)
remove_btn = tkinter.Button(top, text="Remove Time", command=remove, pady=4, padx=4)
confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                             height="5", fg="green")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                             height="5")

tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Day', 'Time', 'Duration'))

tree.heading('#0', text='#')
tree.heading('#1', text='Day')
tree.heading('#2', text='Time')
tree.heading('#3', text='Duration')

tree.column('#0', width="40", anchor=tkinter.CENTER)
tree.column('#1', width=200, anchor=tkinter.CENTER)
tree.column('#2', width=300, anchor=tkinter.CENTER)
tree.column('#3', width=100, anchor=tkinter.CENTER)

if platform.system() == "Windows":

    label.place(x=230, y=10)
    select_day_label.place(x=150, y=75)
    dayList_box.place(x=120, y=100)
    select_time_label.place(x=400, y=75)
    hrs_label.place(x=410, y=100)
    hrs_entry.place(x=395, y=120)
    min_label.place(x=525, y=100)
    min_entry.place(x=515, y=120)
    to_label.place(x=475, y=170)
    hrs2_label.place(x=410, y=200)
    hrs2_entry.place(x=395, y=220)
    mins2_label.place(x=525, y=200)
    mins2_entry.place(x=515, y=220)
    start_label.place(x=350, y=125)
    end_label.place(x=355, y=225)
    add_btn.place(x=600, y=225)
    remove_btn.place(x=680, y=225)
    confirm_btn.place(x=600, y=500)
    back_btn.place(x=400, y=500)
    tree.place(x=70, y=270)

else:

    label.place(x=250, y=30)
    select_day_label.place(x=150, y=75)
    dayList_box.place(x=100, y=100)
    select_time_label.place(x=400, y=75)
    hrs_label.place(x=410, y=100)
    hrs_entry.place(x=395, y=120)
    min_label.place(x=525, y=100)
    min_entry.place(x=515, y=120)
    to_label.place(x=475, y=170)
    hrs2_label.place(x=410, y=200)
    hrs2_entry.place(x=395, y=220)
    mins2_label.place(x=525, y=200)
    mins2_entry.place(x=515, y=220)
    start_label.place(x=350, y=125)
    end_label.place(x=355, y=225)
    add_btn.place(x=600, y=260)
    remove_btn.place(x=680, y=260)
    confirm_btn.place(x=600, y=500)
    back_btn.place(x=400, y=500)
    tree.place(x=70, y=290)

top.mainloop()
