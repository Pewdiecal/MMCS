import tkinter
import os
import platform
from MMCS_DB import validate_user, get_logged_in_user, get_user_position
import multiprocessing

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


class multiProcessWork():

    def s1(self):
        if platform.system() == "Windows":
            os.system('MMCS_registration.py')
        elif platform.system() == "Linux":
            os.system('python3')
        elif platform.system() == "Darwin":
            os.system('python3 ./MMCS_registration.py')

    def s2(self):
        if platform.system() == "Windows":
            os.system('student_main.py')
        elif platform.system() == "Linux":
            os.system('python3')
        elif platform.system() == "Darwin":
            os.system('python3 ./student_main.py')

    def s3(self):
        if platform.system() == "Windows":
            os.system('lecturer_main.py')
        elif platform.system() == "Linux":
            os.system('python3')
        elif platform.system() == "Darwin":
            os.system('python3 ./lecturer_main.py')


def AuthFunc():
    print("login")
    if len(username.get()) > 1 and len(password.get()) > 1:
        if validate_user(username.get(), password.get()):
            if get_user_position(get_logged_in_user()) == "LEC":
                p1s = multiprocessing.Process(target=multiProcessWork().s3, args=())
                p1s.start()
            else:
                p2s = multiprocessing.Process(target=multiProcessWork().s2, args=())
                p2s.start()
        else:
            messagebox.showinfo("Authentication", "Username or password incorrect.")
    else:
        messagebox.showinfo("Authentication", "Please fill in all your credentials.")


def registerFunc():
    p1 = multiprocessing.Process(target=multiProcessWork().s1, args=())
    p1.start()
    print("register")


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
login = tkinter.Button(top, text="Login", command=AuthFunc, pady=4, padx=4, width="20", height="5", fg='green')
register = tkinter.Button(top, text="New User", command=registerFunc, pady=4, padx=4, width="20",
                          height="5")
lableUser = tkinter.Label(top, text="Username")
lablePass = tkinter.Label(top, text="Password")
labelfont = ('Arial', 50, 'bold')
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
username = tkinter.Entry(top, bd=5)
password = tkinter.Entry(top, show="*", bd=5)

if platform.system() == "Windows":
    labelPhoto.place(x=335, y=30)
    labelTitle.place(x=280, y=140)
    lableUser.place(x=275, y=234)
    username.place(x=350, y=230)
    lablePass.place(x=275, y=275)
    password.place(x=350, y=270)
    login.place(x=300, y=310)
    register.place(x=300, y=410)

else:
    labelPhoto.place(x=335, y=30)
    labelTitle.place(x=310, y=140)
    lableUser.place(x=220, y=234)
    username.place(x=295, y=230)
    lablePass.place(x=220, y=275)
    password.place(x=295, y=270)
    login.place(x=300, y=310)
    register.place(x=300, y=410)

top.mainloop()
