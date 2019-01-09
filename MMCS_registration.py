import tkinter
import os
import platform
from MMCS_DB import add_new_user

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)
var = tkinter.StringVar()
var_faculty = tkinter.StringVar()


def back():
    print("back")


def register():
    if room_entry.get() == "":
        add_new_user(fullname_entry.get(), userID_entry.get(), var_faculty.get(), "NULL", pass_entry.get(), var.get())
    elif len(room_entry.get()) >= 2:
        add_new_user(fullname_entry.get(), userID_entry.get(), var_faculty.get(), room_entry.get(), pass_entry.get(), var.get())
    print("register")


def radiobtn():
    if var.get() == "STU":
        room_entry.delete(0, 'end')
        room_entry.configure(state="disabled")
    else:
        room_entry.configure(state="normal")


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
labelfont = ('Arial', 50, 'bold')
label_font_screen = ('Arial', 30)
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
labelScreen = tkinter.Label(top, text="Register New Account", font=label_font_screen)
labelName = tkinter.Label(top, text="Full Name")
fullname_entry = tkinter.Entry(top, bd=5, width=40)
labelUserID = tkinter.Label(top, text="User ID")
userID_entry = tkinter.Entry(top, bd=5)
labelFaculty = tkinter.Label(top, text="Faculty")
FCI_radio = tkinter.Radiobutton(top, text="FCI", value="FCI", variable=var_faculty)
FOM_radio = tkinter.Radiobutton(top, text="FOM", value="FOM", variable=var_faculty)
FOE_radio = tkinter.Radiobutton(top, text="FOE", value="FOE", variable=var_faculty)
FCM_radio = tkinter.Radiobutton(top, text="FCM", value="FCM", variable=var_faculty)
FAC_radio = tkinter.Radiobutton(top, text="FAC", value="FAC", variable=var_faculty)
labelRoom = tkinter.Label(top, text="Room \nNumber")
room_entry = tkinter.Entry(top, bd=5)
labelPass = tkinter.Label(top, text="Password")
pass_entry = tkinter.Entry(top, bd=5, show="*")
labelconfirmPass = tkinter.Label(top, text="Confirm \nPassword")
confirmPass_entry = tkinter.Entry(top, bd=5, show="*")
labelPosition = tkinter.Label(top, text="Position")
lecturer_radio = tkinter.Radiobutton(top, text="Lecturer", value="LEC", variable=var, command=radiobtn)
student_radio = tkinter.Radiobutton(top, text="Student", value="STU", variable=var, command=radiobtn)
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")
register_btn = tkinter.Button(top, text="Register", command=register, pady=4, padx=4, fg='green', width="20",
                              height="5")

if platform.system() == "Windows" :
    labelPhoto.place(x=355, y=20)
    labelTitle.place(x=310, y=120)
    labelScreen.place(x=230, y=195)
    labelName.place(x=250, y=254)
    fullname_entry.place(x=325, y=250)
    labelUserID.place(x=250, y=295)
    userID_entry.place(x=325, y=290)
    labelFaculty.place(x=250, y=330)
    FCI_radio.place(x=325, y=330)
    FCM_radio.place(x=380, y=330)
    FOM_radio.place(x=435, y=330)
    FAC_radio.place(x=490, y=330)
    FOE_radio.place(x=545, y=330)
    labelRoom.place(x=250, y=355)
    room_entry.place(x=325, y=355)
    labelPass.place(x=250, y=400)
    pass_entry.place(x=325, y=395)
    labelconfirmPass.place(x=250, y=430)
    confirmPass_entry.place(x=325, y=433)
    labelPosition.place(x=250, y=475)
    lecturer_radio.place(x=325, y=475)
    student_radio.place(x=430, y=475)
    back_btn.place(x=220, y=505)
    register_btn.place(x=410, y=505)

else:

    labelPhoto.place(x=335, y=30)
    labelTitle.place(x=310, y=140)
    labelScreen.place(x=230, y=200)
    labelName.place(x=250, y=254)
    fullname_entry.place(x=325, y=250)
    labelUserID.place(x=250, y=295)
    userID_entry.place(x=325, y=290)
    labelFaculty.place(x=250, y=330)
    FCI_radio.place(x=325, y=330)
    FCM_radio.place(x=380, y=330)
    FOM_radio.place(x=435, y=330)
    FAC_radio.place(x=490, y=330)
    FOE_radio.place(x=545, y=330)
    labelRoom.place(x=250, y=355)
    room_entry.place(x=325, y=355)
    labelPass.place(x=250, y=400)
    pass_entry.place(x=325, y=395)
    labelconfirmPass.place(x=250, y=430)
    confirmPass_entry.place(x=325, y=433)
    labelPosition.place(x=250, y=475)
    lecturer_radio.place(x=325, y=475)
    student_radio.place(x=430, y=475)
    back_btn.place(x=170, y=505)
    register_btn.place(x=410, y=505)


var.set(0)
var_faculty.set(0)

top.mainloop()
