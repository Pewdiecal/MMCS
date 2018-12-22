import tkinter
from tkinter import ttk as tker

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def back():
    print("back")


label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Student Appointment Status List", font=label_font_screen)
labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
labelName = tkinter.Label(top, text="Lecturer Name: ")
labelTime = tkinter.Label(top, text="Consultation Time: ")
labelDate = tkinter.Label(top, text="Date: Day")
labelFaculty = tkinter.Label(top, text="Faculty: ")
labelRoom = tkinter.Label(top, text="Room Number: ")
labelReason = tkinter.Label(top, text="Cancellation Reason: ")
labelStatus = tkinter.Label(top, text="Status: ")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")


tree = tker.Treeview(top)
tree = tker.Treeview(top, columns=('Lecturer Name', 'Date', 'Time', 'Status'))

tree.heading('#0', text='#')
tree.heading('#1', text='Lecturer Name')
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


label.place(x=180, y=20)
tree.place(x=30, y=60)
labelDetails.place(x=270, y=265)
labelName.place(x=35, y=310)
labelDate.place(x=35, y=330)
labelTime.place(x=35, y=350)
labelStatus.place(x=35, y=370)
labelFaculty.place(x=35, y=390)
labelRoom.place(x=35, y=410)
labelReason.place(x=35, y=430)
back_btn.place(x=300, y=500)

top.mainloop()
