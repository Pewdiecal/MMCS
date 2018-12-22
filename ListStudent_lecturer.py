import tkinter
from tkinter import ttk as tker

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def approve():
    print("approve")


def cancel():
    print("Cancel")


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

# ttt = tree.insert("", 1, text="1", values=("test", "13/12/18", "1pm", "approved"))

for j in range(20):
    tree.insert("", 0, text=str(j), values=("test", "13/12/18", "1pm", "approved"))

# tree.insert(ttt, 1, text="1", values=("test2", "13/12/18", "2pm", "approved"))

label.place(x=235, y=20)
tree.place(x=30, y=60)
labelDetails.place(x=270, y=265)
labelName.place(x=35, y=310)
labelID.place(x=35, y=330)
labelDate.place(x=35, y=350)
labelTime.place(x=35, y=370)
labelStatus.place(x=35, y=390)
labelReason.place(x=35, y=410)
approve_btn.place(x=600, y=500)
cancel_btn.place(x=400, y=500)


top.mainloop()
