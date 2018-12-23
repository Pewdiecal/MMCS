import tkinter
from tkinter import ttk as tker
import os
import platform

top = tkinter.Tk()
if platform.system() == "Windows":
    top.geometry("800x680")
else:
    top.geometry("800x680")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def confirm():
    print("confirm")


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Booking Schedule", font=label_font_screen)
list_label = tkinter.Label(top, text="Select your time")
reason_label = tkinter.Label(top, text="Reason: ")

if platform.system() == "Windows":
    reason_text = tkinter.Text(top, width=73, height=8, highlightbackground="grey")
else:
    reason_text = tkinter.Text(top, width=80, height=8, highlightbackground="grey")

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
    label.place(x=300, y=30)
    list_label.place(x=380, y=100)
    tree.place(x=110, y=150)
    reason_label.place(x=105, y=380)
    reason_text.place(x=165, y=380)
    confirm_btn.place(x=565, y=530)
    back_btn.place(x=365, y=530)

else:
    label.place(x=270, y=30)
    list_label.place(x=330, y=100)
    tree.place(x=75, y=150)
    reason_label.place(x=80, y=360)
    reason_text.place(x=150, y=360)
    confirm_btn.place(x=600, y=500)
    back_btn.place(x=400, y=500)

top.mainloop()
