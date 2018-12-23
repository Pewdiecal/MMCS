import tkinter
from tkinter import ttk as tker
import platform

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def search():
    print("search")


def confirm():
    print("confirm")


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Place Appointment", font=label_font_screen)
if platform.system() == "Windows":
    search = tkinter.Entry(top, bd=5, width=70)
    search_btn = tkinter.Button(top, text="Search", command=search, pady=4, padx=4)
else:
    search = tkinter.Entry(top, bd=5, width=50)
    search_btn = tkinter.Button(top, text="Search", command=search, pady=4, padx=4)
confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20", height="5", fg="green")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")
tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Lecturer Name', 'Room Number'))

tree.heading('#0', text='Lecturer Name')
tree.heading('#1', text='Room Number')
tree.heading('#2', text='Faculty')


tree.column('#0', width=400, anchor=tkinter.CENTER)
tree.column('#1', width=100, anchor=tkinter.CENTER)
tree.column('#2', width=100, anchor=tkinter.CENTER)

if platform.system() == "Windows":
    label.place(x=220, y=20)
    search.place(x=150, y=90)
    search_btn.place(x=590, y=83)
    tree.place(x=95, y=130)
    confirm_btn.place(x=600, y=500)
    back_btn.place(x=10, y=500)
else:
    label.place(x=270, y=20)
    search.place(x=150, y=80)
    search_btn.place(x=620, y=83)
    tree.place(x=95, y=130)
    confirm_btn.place(x=600, y=500)
    back_btn.place(x=10, y=500)


top.mainloop()
