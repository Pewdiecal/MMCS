import tkinter
import os
import platform

top = tkinter.Tk()
top.geometry("800x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)


def back():
    print("back")


def confirm():
    print("confirm")


photo = tkinter.PhotoImage(file="mmu.gif")
labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                          height="5")
labelfont = ('Arial', 50, 'bold')
label_font_screen = ('Arial', 30)
labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
labelScreen = tkinter.Label(top, text="Credential Settings", font=label_font_screen)
labelOldPass = tkinter.Label(top, text="Old Password")
oldPass_entry = tkinter.Entry(top, bd=5, show="*")
labelNewPass = tkinter.Label(top, text="New Password")
newPass_entry = tkinter.Entry(top, bd=5, show="*")
labelConfirmPass = tkinter.Label(top, text="Confirm Password")
confirmPass_entry = tkinter.Entry(top, bd=5, show="*")
confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                             height="5", fg='green')

if platform.system() == "Windows":
    labelPhoto.place(x=360, y=20)
    back_btn.place(x=200, y=370)
    labelTitle.place(x=310, y=120)
    labelScreen.place(x=250, y=190)
    labelOldPass.place(x=295, y=254)
    oldPass_entry.place(x=380, y=250)
    labelNewPass.place(x=290, y=294)
    newPass_entry.place(x=380, y=290)
    labelConfirmPass.place(x=270, y=334)
    confirmPass_entry.place(x=380, y=330)
    confirm_btn.place(x=400, y=370)

else:

    labelPhoto.place(x=335, y=40)
    back_btn.place(x=200, y=370)
    labelTitle.place(x=310, y=140)
    labelScreen.place(x=250, y=200)
    labelOldPass.place(x=220, y=254)
    oldPass_entry.place(x=325, y=250)
    labelNewPass.place(x=220, y=294)
    newPass_entry.place(x=325, y=290)
    labelConfirmPass.place(x=200, y=334)
    confirmPass_entry.place(x=325, y=330)
    confirm_btn.place(x=400, y=370)

top.mainloop()
