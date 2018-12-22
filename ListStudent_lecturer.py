import tkinter
from tkinter import ttk as tker

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)

label_font_screen = ('Arial', 30)
label = tkinter.Label(top, text="Student Appointment List", font=label_font_screen)
labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
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

top.mainloop()
