import tkinter

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)
var = tkinter.StringVar()


def back():
    print("back")


def register():
    print("register")


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
labelfont = ('Arial', 50, 'bold')
label_font_screen = ('Arial', 30)
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
labelScreen = tkinter.Label(top, text="Register New Account", font=label_font_screen)
labelName = tkinter.Label(top, text="Full Name")
fullname_entry = tkinter.Entry(top, bd=5)
labelUserID = tkinter.Label(top, text="User ID")
userID_entry = tkinter.Entry(top, bd=5)
labelPass = tkinter.Label(top, text="Password")
pass_entry = tkinter.Entry(top, bd=5, show="*")
labelconfirmPass = tkinter.Label(top, text="Confirm \nPassword")
confirmPass_entry = tkinter.Entry(top, bd=5, show="*")
labelPosition = tkinter.Label(top, text="Position")
lecturer_radio = tkinter.Radiobutton(top, text="Lecturer", value=1, variable=var)
student_radio = tkinter.Radiobutton(top, text="Student", value=2, variable=var)
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")
register_btn = tkinter.Button(top, text="Register", command=register, pady=4, padx=4, fg='green', width="20",
                              height="5")

labelPhoto.place(x=335, y=30)
labelTitle.place(x=310, y=140)
labelScreen.place(x=230, y=200)
labelName.place(x=250, y=254)
fullname_entry.place(x=325, y=250)
labelUserID.place(x=250, y=295)
userID_entry.place(x=325, y=290)
labelPass.place(x=250, y=336)
pass_entry.place(x=325, y=330)
labelconfirmPass.place(x=250, y=368)
confirmPass_entry.place(x=325, y=370)
labelPosition.place(x=250, y=410)
lecturer_radio.place(x=325, y=410)
student_radio.place(x=430, y=410)
back_btn.place(x=170, y=450)
register_btn.place(x=410, y=450)


top.mainloop()
