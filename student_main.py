import tkinter

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def add_edit():
    print("add/edit")


def lists():
    print("student list")


def logout():
    print("logout")


def exit():
    print("exit")


def changePass():
    print("change pass")


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
label_font = ('Arial', 20, 'bold')
labelfont = ('Arial', 50, 'bold')
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
label_user = tkinter.Label(top, text="Welcome, USER_NAME", font=label_font)
add_edit_btn = tkinter.Button(top, text="Place Appointment", command=add_edit, pady=4, padx=4, width="20", height="5")
student_list_btn = tkinter.Button(top, text="Check Status", command=lists, pady=4, padx=4, width="20", height="5")
logout_btn = tkinter.Button(top, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
exit_btn = tkinter.Button(top, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
changePass_btn = tkinter.Button(top, text="Credential Settings", command=changePass, pady=4, padx=4, width="20", height="5")

labelPhoto.place(x=335, y=30)
labelTitle.place(x=310, y=130)
label_user.place(y=200)
add_edit_btn.place(x=300, y=270)
student_list_btn.place(x=300, y=370)
logout_btn.place(y=510)
exit_btn.place(x=200, y=510)
changePass_btn.place(x=610, y=510)

top.mainloop()