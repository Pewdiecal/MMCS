import tkinter
from tkinter import ttk as tker
import os
import platform

top = tkinter.Tk()
top.geometry("900x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Student Appointment Status List", font=label_font_screen)
labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
labelName = tkinter.Label(top, text="Lecturer Name: ")
labelTime = tkinter.Label(top, text="Consultation Time: ")
labelDate = tkinter.Label(top, text="Date: ")
labelFaculty = tkinter.Label(top, text="Faculty: ")
labelRoom = tkinter.Label(top, text="Room Number: ")
labelReason = tkinter.Label(top, text="Cancellation Reason: ")
labelStatus = tkinter.Label(top, text="Status: ")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")


tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Lecturer Name', 'Day', 'Time', 'ID' ,'Status'))

tree.heading('#0', text='#')
tree.heading('#1', text='Lecturer Name')
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
tree.insert("", 'end', text=str("0"), values=("test", "13/12/18", "1pm", "MU131313","approved"))
tree.insert("", 'end', text=str("1"), values=("test1", "13/12/18", "1pm", "MU0000","approved"))
tree.insert("", 'end', text=str("2"), values=("test2", "13/12/18", "1pm", "MU5544","approved"))
tree.insert("", 'end', text=str("3"), values=("test3", "13/12/18", "1pm", "MU6666","approved"))
tree.insert("", 'end', text=str("4"), values=("test4", "13/12/18", "1pm", "MU9090","approved"))


if platform.system() == "Windows":
    label.place(x=108, y=5)
    tree.place(x=30, y=60)
    labelDetails.place(x=220, y=280)
    labelName.place(x=35, y=330)
    labelDate.place(x=35, y=355)
    labelTime.place(x=35, y=380)
    labelStatus.place(x=35, y=405)
    labelFaculty.place(x=35, y=430)
    labelRoom.place(x=35, y=455)
    labelReason.place(x=35, y=480)
    back_btn.place(x=640, y=500)

else:
    label.place(x=210, y=20)
    tree.place(x=30, y=60)
    labelDetails.place(x=290, y=265)
    labelName.place(x=35, y=310)
    labelDate.place(x=35, y=330)
    labelTime.place(x=35, y=350)
    labelStatus.place(x=35, y=370)
    labelFaculty.place(x=35, y=390)
    labelRoom.place(x=35, y=410)
    labelReason.place(x=35, y=430)
    back_btn.place(x=350, y=500)




top.mainloop()
