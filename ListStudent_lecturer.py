import tkinter
from tkinter import ttk as tker
import os
import platform

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def approve():
    print("approve")


def cancel():
    print("Cancel")


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Student Appointment List", font=label_font_screen)
labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
labelName = tkinter.Label(top, text="Student Name: ")
labelID = tkinter.Label(top, text="ID: ")
labelTime = tkinter.Label(top, text="Consultation Time: ")
labelDate = tkinter.Label(top, text="Date: Day")
labelReason = tkinter.Label(top, text="Reason: ")
labelStatus = tkinter.Label(top, text="Status: ")
approve_btn = tkinter.Button(top, text="Confirm Appointment", command=approve, pady=4, padx=4, width="20", height="5", fg="green")
cancel_btn = tkinter.Button(top, text="Cancel Appointment", command=cancel, pady=4, padx=4, width="20", height="5", fg="red")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")
tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Name', 'Date', 'Time', 'Status'))

tree.heading('#0', text='#')
tree.heading('#1', text='Name')
tree.heading('#2', text='Date')
tree.heading('#3', text='Time')
tree.heading('#4', text='Status')

tree.column('#0', width="40", anchor=tkinter.CENTER)
tree.column('#1', width=400, anchor=tkinter.CENTER)
tree.column('#2', width=100, anchor=tkinter.CENTER)
tree.column('#3', width=100, anchor=tkinter.CENTER)
tree.column('#4', width=100, anchor=tkinter.CENTER)


for j in range(20):
    tree.insert("", 0, text=str(j), values=("test", "13/12/18", "1pm", "approved"))

if platform.system() == "Windows":
    label.place(x=190, y=5)
    tree.place(x=30, y=60)
    labelDetails.place(x=245, y=280)
    labelName.place(x=35, y=330)
    labelID.place(x=35, y=355)
    labelDate.place(x=35, y=380)
    labelTime.place(x=35, y=405)
    labelStatus.place(x=35, y=430)
    labelReason.place(x=35, y=455)
    approve_btn.place(x=600, y=500)
    cancel_btn.place(x=400, y=500)
    back_btn.place(x=10, y=500)

else:

    label.place(x=190, y=5)
    tree.place(x=30, y=60)
    labelDetails.place(x=270, y=280)
    labelName.place(x=35, y=330)
    labelID.place(x=35, y=355)
    labelDate.place(x=35, y=380)
    labelTime.place(x=35, y=405)
    labelStatus.place(x=35, y=430)
    labelReason.place(x=35, y=455)
    approve_btn.place(x=600, y=500)
    cancel_btn.place(x=400, y=500)
    back_btn.place(x=10, y=500)



top.mainloop()
