import tkinter
from tkinter import ttk as tker
import os
import platform

top = tkinter.Tk()
top.geometry("900x600")
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
labelDate = tkinter.Label(top, text="Date: ")
labelReason = tkinter.Label(top, text="Reason: ")
labelStatus = tkinter.Label(top, text="Faculty: ")
approve_btn = tkinter.Button(top, text="Confirm Appointment", command=approve, pady=4, padx=4, width="20", height="2", fg="green")
cancel_btn = tkinter.Button(top, text="Cancel Appointment", command=cancel, pady=4, padx=4, width="20", height="2", fg="red")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="2")
tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Name', 'Day', 'Time', 'ID', 'Status'))

tree.heading('#0', text='#')
tree.heading('#1', text='Name')
tree.heading('#2', text='Day')
tree.heading('#3', text='Time')
tree.heading('#4', text='ID')
tree.heading('#5', text='Status')

tree.column('#0', width="40", anchor=tkinter.CENTER)
tree.column('#1', width=400, anchor=tkinter.CENTER)
tree.column('#2', width=100, anchor=tkinter.CENTER)
tree.column('#3', width=100, anchor=tkinter.CENTER)
tree.column('#4', width=100, anchor=tkinter.CENTER)
tree.column('#5', width=100, anchor=tkinter.CENTER)


def selectItem(a):
    curItem = tree.focus()
    #print(tree.item(curItem))
    values = tree.item(curItem)
    stu_ids = values['values']
    print(stu_ids[3]) # output selected lec's id


tree.bind('<Double-Button-1>', selectItem)

for j in range(20):
    tree.insert("", 0, text=str(j), values=("test", "13/12/18", "1pm", "1123345566", "approved"))


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
    approve_btn.place(x=600, y=550)
    cancel_btn.place(x=400, y=550)
    back_btn.place(x=10, y=550)

else:

    label.place(x=260, y=5)
    tree.place(x=30, y=60)
    labelDetails.place(x=290, y=280)
    labelName.place(x=35, y=330)
    labelID.place(x=35, y=355)
    labelDate.place(x=35, y=380)
    labelTime.place(x=35, y=405)
    labelStatus.place(x=35, y=430)
    labelReason.place(x=35, y=455)
    approve_btn.place(x=700, y=550)
    cancel_btn.place(x=500, y=550)
    back_btn.place(x=10, y=550)

top.mainloop()
