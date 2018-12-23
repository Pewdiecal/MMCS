import tkinter
import os
import platform

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)
os.chdir(os.path.dirname(__file__))


def add_edit():
    print("add/edit")
    if platform.system() == "Windows":
        os.system('addTime_lecturer.py')
    elif platform.system() == "Linux":
        os.system('python3')
    elif platform.system() == "Darwin":
        os.system('python3 ./addTime_lecturer.py')


def lists():
    print("student list")
    if platform.system() == "Windows":
        os.system('ListStudent_lecturer.py')
    elif platform.system() == "Linux":
        os.system('python3')
    elif platform.system() == "Darwin":
        os.system('python3 ./ListStudent_lecturer.py')


def logout():
    print("logout")


def exit():
    print("exit")


def changePass():
    print("change pass")
    if platform.system() == "Windows":
        os.system('changePass.py')
    elif platform.system() == "Linux":
        os.system('python3')
    elif platform.system() == "Darwin":
        os.system('python3 ./changePass.py')


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
label_font = ('Arial', 20, 'bold')
labelfont = ('Arial', 50, 'bold')
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
label_user = tkinter.Label(top, text="Welcome, USER_NAME", font=label_font)
add_edit_btn = tkinter.Button(top, text="Add/Edit Schedule", command=add_edit, pady=4, padx=4, width="20", height="5")
student_list_btn = tkinter.Button(top, text="List Of Students", command=lists, pady=4, padx=4, width="20", height="5")
logout_btn = tkinter.Button(top, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
exit_btn = tkinter.Button(top, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
changePass_btn = tkinter.Button(top, text="Credential Settings", command=changePass, pady=4, padx=4, width="20",
                                height="5")

if platform.system() == "Windows":
    labelPhoto.place(x=360, y=30)
    labelTitle.place(x=310, y=130)
    label_user.place(y=200)
    add_edit_btn.place(x=360, y=270)
    student_list_btn.place(x=360, y=370)
    logout_btn.place(y=510)
    exit_btn.place(x=160, y=510)
    changePass_btn.place(x=640, y=510)

else:
    labelPhoto.place(x=335, y=30)
    labelTitle.place(x=310, y=130)
    label_user.place(y=200)
    add_edit_btn.place(x=300, y=270)
    student_list_btn.place(x=300, y=370)
    logout_btn.place(y=510)
    exit_btn.place(x=200, y=510)
    changePass_btn.place(x=610, y=510)



top.mainloop()
