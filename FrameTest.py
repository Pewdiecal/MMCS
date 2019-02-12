import tkinter
import os
import platform
from tkinter import messagebox
from tkinter import ttk as tker
from MMCS_DB import *
from datetime import date
import calendar

top = tkinter.Tk()
top.geometry("900x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)
photo = tkinter.PhotoImage(file="mmu.gif")


def MMCS_Auth():
    def AuthFunc():
        print("login")
        if len(username.get()) > 1 and len(password.get()) > 1:
            if validate_user(username.get(), password.get()):
                for widget in top.winfo_children():
                    widget.destroy()
                mainFrames()
            else:
                messagebox.showinfo("Authentication", "Username or password incorrect.")

        else:
            messagebox.showinfo("Authentication", "Please fill in all your credentials.")

    def registerFunc():
        for widget in top.winfo_children():
            widget.destroy()
        MMCS_registration()
        print("register")

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
        labelPhoto.place(x=445, y=30)
        labelTitle.place(x=413, y=140)
        lableUser.place(x=325, y=234)
        username.place(x=400, y=230)
        lablePass.place(x=325, y=275)
        password.place(x=400, y=270)
        login.place(x=405, y=310)
        register.place(x=405, y=410)


class mainFrames(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tkinter.Frame(top)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.update()
        self.destroy()
        if get_user_position(get_logged_in_user()) == "LEC":  # launch required frames according to user
            for F in (addTime_lec, change_pass, listStudent_lecturer, lecturer_main):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("lecturer_main")
        else:
            for F in (appointmentList_stu, booking_student,
                      change_pass, student_main,
                      addAppointment_stu):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame("student_main")

    def show_frame(self, page_name):

        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class addTime_lec(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        def add():
            getDate()
            day = dayList_box.get(dayList_box.curselection())
            time_start = hrs_entry.get() + ':' + min_entry.get()
            time_end = hrs2_entry.get() + ':' + mins2_entry.get()
            add_lec_time(get_logged_in_user(), day, time_start, time_end, )
            print("add")

        def remove():
            print("remove")

        def confirm():
            print("confirm")
            controller.show_frame("lecturer_main")

        def back():
            print("back")
            controller.show_frame("lecturer_main")

        label_font_screen = ('Arial', 30)
        label = tkinter.Label(self, text="Schedule Availability", font=label_font_screen)
        select_day_label = tkinter.Label(self, text="Select Day")
        select_time_label = tkinter.Label(self, text="Select Time (24Hrs format)")
        dayList_box = tkinter.Listbox(self)
        dayList_box.insert(1, "Monday")
        dayList_box.insert(2, "Tuesday")
        dayList_box.insert(3, "Wednesday")
        dayList_box.insert(4, "Thursday")
        dayList_box.insert(5, "Friday")
        hrs_label = tkinter.Label(self, text="Hrs")
        hrs_entry = tkinter.Entry(self, bd=5, width=5)
        min_label = tkinter.Label(self, text="Mins")
        min_entry = tkinter.Entry(self, bd=5, width=5)
        hrs2_label = tkinter.Label(self, text="Hrs")
        hrs2_entry = tkinter.Entry(self, bd=5, width=5)
        mins2_label = tkinter.Label(self, text="Mins")
        mins2_entry = tkinter.Entry(self, bd=5, width=5)
        start_label = tkinter.Label(self, text="Start")
        end_label = tkinter.Label(self, text="End")
        to_label = tkinter.Label(self, text="To")
        add_btn = tkinter.Button(self, text="Add Time", command=add, pady=4, padx=4)
        remove_btn = tkinter.Button(self, text="Remove Time", command=remove, pady=4, padx=4)
        confirm_btn = tkinter.Button(self, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                                     height="5", fg="green")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="5")

        tree = tker.Treeview(self)
        tree = tker.Treeview(self, columns=('Day', 'Time', 'Duration'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='Day')
        tree.heading('#2', text='Time')
        tree.heading('#3', text='Duration')

        tree.column('#0', width=40, anchor=tkinter.CENTER)
        tree.column('#1', width=200, anchor=tkinter.CENTER)
        tree.column('#2', width=300, anchor=tkinter.CENTER)
        tree.column('#3', width=100, anchor=tkinter.CENTER)

        if platform.system() == "Windows":

            label.place(x=230, y=10)
            select_day_label.place(x=150, y=75)
            dayList_box.place(x=120, y=100)
            select_time_label.place(x=400, y=75)
            hrs_label.place(x=410, y=100)
            hrs_entry.place(x=395, y=120)
            min_label.place(x=525, y=100)
            min_entry.place(x=515, y=120)
            to_label.place(x=475, y=170)
            hrs2_label.place(x=410, y=200)
            hrs2_entry.place(x=395, y=220)
            mins2_label.place(x=525, y=200)
            mins2_entry.place(x=515, y=220)
            start_label.place(x=350, y=125)
            end_label.place(x=355, y=225)
            add_btn.place(x=600, y=225)
            remove_btn.place(x=680, y=225)
            confirm_btn.place(x=600, y=500)
            back_btn.place(x=400, y=500)
            tree.place(x=70, y=270)

        else:

            label.place(x=360, y=30)
            select_day_label.place(x=280, y=75)
            dayList_box.place(x=230, y=100)
            select_time_label.place(x=635, y=75)
            hrs_label.place(x=650, y=100)
            hrs_entry.place(x=635, y=120)
            min_label.place(x=765, y=100)
            min_entry.place(x=755, y=120)
            to_label.place(x=710, y=170)
            hrs2_label.place(x=650, y=200)
            hrs2_entry.place(x=635, y=220)
            mins2_label.place(x=765, y=200)
            mins2_entry.place(x=755, y=220)
            start_label.place(x=590, y=125)
            end_label.place(x=595, y=225)
            add_btn.place(x=665, y=260)
            remove_btn.place(x=745, y=260)
            confirm_btn.place(x=650, y=500)
            back_btn.place(x=450, y=500)
            tree.place(x=200, y=290)


class appointmentList_stu(tkinter.Frame):  # CRASH

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def back():
            print("back")
            controller.show_frame("student_main")

        label_font_screen = ('Arial', 30)
        label = tkinter.Label(self, text="Student Appointment Status List", font=label_font_screen)
        labelDetails = tkinter.Label(self, text="Appointment Details", font=label_font_screen)
        labelName = tkinter.Label(self, text="Lecturer Name: ")
        labelTime = tkinter.Label(self, text="Consultation Time: ")
        labelDate = tkinter.Label(self, text="Date: ")
        labelFaculty = tkinter.Label(self, text="Faculty: ")
        labelRoom = tkinter.Label(self, text="Room Number: ")
        labelReason = tkinter.Label(self, text="Cancellation Reason: ")
        labelStatus = tkinter.Label(self, text="Status: ")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="5")

        tree = tker.Treeview(self)
        tree = tker.Treeview(self, columns=('Lecturer Name', 'Day', 'Time', 'ID', 'Status'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='Lecturer Name')
        tree.heading('#2', text='Day')
        tree.heading('#3', text='Time')
        tree.heading('#4', text='ID')
        tree.heading('#5', text='Status')

        tree.column('#0', width=40, anchor=tkinter.CENTER)
        tree.column('#1', width=400, anchor=tkinter.CENTER)
        tree.column('#2', width=100, anchor=tkinter.CENTER)
        tree.column('#3', width=100, anchor=tkinter.CENTER)
        tree.column('#4', width=100, anchor=tkinter.CENTER)
        tree.column('#5', width=100, anchor=tkinter.CENTER)

        def selectItem(a):
            curItem = tree.focus()
            # print(tree.item(curItem))
            values = tree.item(curItem)
            stu_ids = values['values']
            print(stu_ids[3])  # output selected lec's id

        tree.bind('<Double-Button-1>', selectItem)
        tree.insert("", 'end', text=str("0"), values=("test", "13/12/18", "1pm", "MU131313", "approved"))
        tree.insert("", 'end', text=str("1"), values=("test1", "13/12/18", "1pm", "MU0000", "approved"))
        tree.insert("", 'end', text=str("2"), values=("test2", "13/12/18", "1pm", "MU5544", "approved"))
        tree.insert("", 'end', text=str("3"), values=("test3", "13/12/18", "1pm", "MU6666", "approved"))
        tree.insert("", 'end', text=str("4"), values=("test4", "13/12/18", "1pm", "MU9090", "approved"))

        if platform.system() == "Windows":
            label.place(x=170, y=5)
            tree.place(x=30, y=60)
            labelDetails.place(x=275, y=280)
            labelName.place(x=35, y=330)
            labelDate.place(x=35, y=355)
            labelTime.place(x=35, y=380)
            labelStatus.place(x=35, y=405)
            labelFaculty.place(x=35, y=430)
            labelRoom.place(x=35, y=455)
            labelReason.place(x=35, y=480)
            back_btn.place(x=640, y=500)

        else:
            label.place(x=280, y=20)
            tree.place(x=80, y=60)
            labelDetails.place(x=360, y=265)
            labelName.place(x=75, y=310)
            labelDate.place(x=75, y=330)
            labelTime.place(x=75, y=350)
            labelStatus.place(x=75, y=370)
            labelFaculty.place(x=75, y=390)
            labelRoom.place(x=75, y=410)
            labelReason.place(x=75, y=430)
            back_btn.place(x=405, y=540)


class booking_student(tkinter.Frame):  # FIX

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def confirm():
            print("confirm")
            controller.show_frame("student_main")

        def back():
            print("back")
            controller.show_frame("addAppointment_stu")

        label_font_screen = ('Arial', 30)
        label = tkinter.Label(self, text="Booking Schedule", font=label_font_screen)
        list_label = tkinter.Label(self, text="Select your time")
        reason_label = tkinter.Label(self, text="Reason: ")
        if platform.system() == "Windows":
            reason_text = tkinter.Text(self, width=73, height=8, highlightbackground="grey")
        else:
            reason_text = tkinter.Text(self, width=80, height=8, highlightbackground="grey")

        confirm_btn = tkinter.Button(self, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                                     height="2", fg="green")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="2")

        tree = tker.Treeview(self)
        tree = tker.Treeview(self, columns=('Day', 'Time', 'Duration'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='Day')
        tree.heading('#2', text='Time')
        tree.heading('#3', text='Duration')

        tree.column('#0', width="40", anchor=tkinter.CENTER)
        tree.column('#1', width=200, anchor=tkinter.CENTER)
        tree.column('#2', width=300, anchor=tkinter.CENTER)
        tree.column('#3', width=100, anchor=tkinter.CENTER)

        if platform.system() == "Windows":
            label.place(x=275, y=30)
            list_label.place(x=380, y=100)
            tree.place(x=110, y=150)
            reason_label.place(x=105, y=380)
            reason_text.place(x=165, y=380)
            confirm_btn.place(x=595, y=520)
            back_btn.place(x=430, y=520)

        else:
            label.place(x=270, y=30)
            list_label.place(x=330, y=100)
            tree.place(x=75, y=150)
            reason_label.place(x=80, y=360)
            reason_text.place(x=150, y=360)
            confirm_btn.place(x=600, y=500)
            back_btn.place(x=400, y=500)


class change_pass(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def back():
            if get_user_position(get_logged_in_user()) == "LEC":
                controller.show_frame("lecturer_main")
            else:
                controller.show_frame("student_main")
            print("back")

        def confirm():
            if oldPass_entry.get() != "" and newPass_entry.get() != "" and confirmPass_entry.get() != "":
                if len(newPass_entry.get()) >= 8:
                    if newPass_entry.get() == confirmPass_entry.get():
                        if update_user_password(get_logged_in_user(), oldPass_entry.get(), newPass_entry.get()):
                            messagebox.showinfo("Credential Settings", "Password Changed.")
                            oldPass_entry.delete(0, 'end')
                            newPass_entry.delete(0, 'end')
                            confirmPass_entry.delete(0, 'end')
                            if get_user_position(get_logged_in_user()) == "LEC":
                                controller.show_frame("lecturer_main")
                            else:
                                controller.show_frame("student_main")
                        else:
                            messagebox.showerror("Credential Settings", "Invalid old password.")
                    else:
                        messagebox.showerror("Credential Settings",
                                             "New password does not match with confirm password.")
                else:
                    messagebox.showerror("Credential Settings", "Password must be at least 8 characters.")
            else:
                messagebox.showerror("Credential Settings", "Please fill in all your credentials.")
            print("confirm")

        labelPhoto = tkinter.Label(self, image=photo, width="100", height="100")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="5")
        labelfont = ('Arial', 50, 'bold')
        label_font_screen = ('Arial', 30)
        labelTitle = tkinter.Label(self, text="MMCS", font=labelfont)
        labelScreen = tkinter.Label(self, text="Credential Settings", font=label_font_screen)
        labelOldPass = tkinter.Label(self, text="Old Password")
        oldPass_entry = tkinter.Entry(self, bd=5, show="*")
        labelNewPass = tkinter.Label(self, text="New Password")
        newPass_entry = tkinter.Entry(self, bd=5, show="*")
        labelConfirmPass = tkinter.Label(self, text="Confirm Password")
        confirmPass_entry = tkinter.Entry(self, bd=5, show="*")
        confirm_btn = tkinter.Button(self, text="Confirm", command=confirm, pady=4, padx=4, width="20",
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


class lecturer_main(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        print("Lecturer main RUNNING")

        def add_edit():
            print("add/edit")
            controller.show_frame("addTime_lec")

        def lists():
            print("student list")
            controller.show_frame("listStudent_lecturer")

        def logout():
            logout_user()
            for widget in top.winfo_children():
                widget.destroy()
            MMCS_Auth()
            print("logout")

        def exit():
            logout_user()
            top.destroy()
            print("exit")

        def changePass():
            print("change pass")
            controller.show_frame("change_pass")

        labelPhoto = tkinter.Label(self, image=photo, width="100", height="100")
        label_font = ('Arial', 20, 'bold')
        labelfont = ('Arial', 50, 'bold')
        labelTitle = tkinter.Label(self, text="MMCS", font=labelfont)

        label_user = tkinter.Label(self, text="Welcome, " + get_user_name(get_logged_in_user()), font=label_font)
        add_edit_btn = tkinter.Button(self, text="Add/Edit Schedule", command=add_edit, pady=4, padx=4, width="20",
                                      height="5")
        student_list_btn = tkinter.Button(self, text="List Of Students", command=lists, pady=4, padx=4, width="20",
                                          height="5")
        logout_btn = tkinter.Button(self, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
        exit_btn = tkinter.Button(self, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
        changePass_btn = tkinter.Button(self, text="Credential Settings", command=changePass, pady=4, padx=4,
                                        width="20",
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


class listStudent_lecturer(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def approve():
            curItem = tree.focus()
            values = tree.item(curItem)
            stu_ids = values['values']
            try:
                update_approval_status(stu_ids[3], get_logged_in_user(), stu_ids[1], True)
                print("TREE :", tree.get_children())
                for i in tree.get_children():
                    tree.delete(i)
                for j in range(6):
                    full_array = (get_all_lec_bookings(get_logged_in_user()))[j]
                    tree.insert("", 'end', text=str(j),
                                values=(full_array[0], full_array[3], full_array[2], full_array[5], full_array[4]))

                print("approve")
            except IndexError as error:
                messagebox.showerror("MMCS", "Please select a student to Approve.")

        def cancel():
            curItem = tree.focus()
            values = tree.item(curItem)
            stu_ids = values['values']
            try:
                update_approval_status(stu_ids[3], get_logged_in_user(), stu_ids[1], False)
                for i in tree.get_children():
                    tree.delete(i)
                for j in range(6):
                    full_array = (get_all_lec_bookings(get_logged_in_user()))[j]
                    tree.insert("", 'end', text=str(j),
                                values=(full_array[0], full_array[3], full_array[2], full_array[5], full_array[4]))
                print("Cancel")
            except IndexError as error:
                messagebox.showerror("MMCS", "Please select a student to Cancel.")

        def back():
            print("back")
            controller.show_frame("lecturer_main")

        label_font_screen = ('Arial', 30)
        label = tkinter.Label(self, text="Student Appointment List", font=label_font_screen)
        labelDetails = tkinter.Label(self, text="Appointment Details", font=label_font_screen)
        labelName = tkinter.Label(self, text="Student Name: ")
        labelID = tkinter.Label(self, text="ID: ")
        labelTime = tkinter.Label(self, text="Consultation Time: ")
        labelDate = tkinter.Label(self, text="Date: ")
        labelReason = tkinter.Label(self, text="Reason: ")
        labelFaculty = tkinter.Label(self, text="Faculty: ")
        approve_btn = tkinter.Button(self, text="Confirm Appointment", command=approve, pady=4, padx=4, width="20",
                                     height="2", fg="green")
        cancel_btn = tkinter.Button(self, text="Cancel Appointment", command=cancel, pady=4, padx=4, width="20",
                                    height="2", fg="red")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="2")
        tree = tker.Treeview(self)
        tree = tker.Treeview(self, columns=('Name', 'Day', 'Time', 'ID', 'Status'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='Name')
        tree.heading('#2', text='Day')
        tree.heading('#3', text='Time')
        tree.heading('#4', text='ID')
        tree.heading('#5', text='Status')

        tree.column('#0', width=40, anchor=tkinter.CENTER)
        tree.column('#1', width=400, anchor=tkinter.CENTER)
        tree.column('#2', width=100, anchor=tkinter.CENTER)
        tree.column('#3', width=100, anchor=tkinter.CENTER)
        tree.column('#4', width=100, anchor=tkinter.CENTER)
        tree.column('#5', width=100, anchor=tkinter.CENTER)

        def selectItem(a):
            curItem = tree.focus()
            values = tree.item(curItem)
            stu_ids = values['values']
            labelName.config(text="Student Name: " + str(get_user_name(str(stu_ids[3]))))
            labelID.config(text="ID: " + str(stu_ids[3]))
            labelDate.config(text="Date: " + str(stu_ids[1]))
            labelTime.config(text="Consultation Time: " + str(stu_ids[2]))
            labelFaculty.config(text="Faculty: " + str(get_user_faculty(str(stu_ids[3]))))
            labelReason.config(text="Reason: " + str(get_user_reason(str(stu_ids[3]), str(get_logged_in_user()))))

        tree.bind('<Double-Button-1>', selectItem)

        for j in range(len(get_all_lec_bookings(get_logged_in_user()))):
            full_array = (get_all_lec_bookings(get_logged_in_user()))[j]
            tree.insert("", 'end', text=str(j),
                        values=(full_array[0], full_array[3], full_array[2], full_array[5], full_array[4]))

        if platform.system() == "Windows":
            label.place(x=190, y=5)
            tree.place(x=30, y=60)
            labelDetails.place(x=245, y=280)
            labelName.place(x=35, y=330)
            labelID.place(x=35, y=355)
            labelDate.place(x=35, y=380)
            labelTime.place(x=35, y=405)
            labelFaculty.place(x=35, y=430)
            labelReason.place(x=35, y=455)
            approve_btn.place(x=600, y=550)
            cancel_btn.place(x=400, y=550)
            back_btn.place(x=10, y=550)

        else:

            label.place(x=260, y=5)
            tree.place(x=30, y=60)
            labelDetails.place(x=290, y=280)
            labelName.place(x=35, y=330)
            labelID.place(x=35, y=355)
            labelDate.place(x=35, y=380)
            labelTime.place(x=35, y=405)
            labelFaculty.place(x=35, y=430)
            labelReason.place(x=35, y=455)
            approve_btn.place(x=700, y=550)
            cancel_btn.place(x=500, y=550)
            back_btn.place(x=10, y=550)


def MMCS_registration():
    var = tkinter.StringVar()
    var_faculty = tkinter.StringVar()

    def back():
        for widget in top.winfo_children():
            widget.destroy()
        MMCS_Auth()
        print("back")

    def register():
        if var.get() == "LEC":

            if len(fullname_entry.get()) <= 1 or len(userID_entry.get()) <= 1 or len(var_faculty.get()) <= 1 or len(
                    room_entry.get()) <= 1:
                messagebox.showerror("Error", "Please fill up all the necessary informations.")
            else:
                if len(pass_entry.get()) >= 8:
                    if pass_entry.get() == confirmPass_entry.get():
                        if check_user_id(userID_entry.get()):

                            add_new_user(fullname_entry.get(), userID_entry.get(), var_faculty.get(),
                                         room_entry.get(),
                                         pass_entry.get(), var.get())
                            messagebox.showinfo("Registration", "Registration successful.")
                            for widget in top.winfo_children():
                                widget.destroy()
                            MMCS_Auth()
                        else:
                            messagebox.showerror("Error",
                                                 "The User ID had already exists in the database. Please enter a different ID.")
                    else:
                        messagebox.showerror("Error",
                                             "Password does not match. Please try again.")
                else:
                    messagebox.showerror("Error",
                                         "Password must be atleast 8 characters long. Please try again.")
        elif var.get() == "STU":

            if len(fullname_entry.get()) >= 1 or len(userID_entry.get()) >= 1 or len(var_faculty.get()) >= 1:
                if len(pass_entry.get()) >= 8:
                    if pass_entry.get() == confirmPass_entry.get():
                        if check_user_id(userID_entry.get()):

                            add_new_user(fullname_entry.get(), userID_entry.get(), var_faculty.get(), "NULL",
                                         pass_entry.get(), var.get())

                            messagebox.showinfo("Registration", "Registration successful.")
                            for widget in top.winfo_children():
                                widget.destroy()
                            MMCS_Auth()

                        else:
                            messagebox.showerror("Error",
                                                 "The User ID had already exists in the database. Please enter a different ID.")
                    else:
                        messagebox.showerror("Error",
                                             "Password does not match. Please try again.")
                else:
                    messagebox.showerror("Error",
                                         "Password must be atleast 8 characters long. Please try again.")
            else:
                messagebox.showerror("Error", "Please fill up all the necessary informations.")

        else:
            messagebox.showerror("Error", "Please fill up all the necessary informations.")

        print("register")

    def radiobtn():
        if var.get() == "STU":
            room_entry.delete(0, 'end')
            room_entry.configure(state="disabled")
        else:
            room_entry.configure(state="normal")

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

    if platform.system() == "Windows":
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


class student_main(tkinter.Frame):  # CRASH

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def add_edit():
            print("place appointment")
            controller.show_frame("addAppointment_stu")

        def lists():
            print("student list")
            controller.show_frame("appointmentList_stu")

        def logout():
            logout_user()
            for widget in top.winfo_children():
                widget.destroy()
            MMCS_Auth()
            print("logout")

        def exit():
            logout_user()
            top.destroy()
            print("logout")

        def changePass():
            print("change pass")
            controller.show_frame("change_pass")

        labelPhoto = tkinter.Label(self, image=photo, width="100", height="100")
        label_font = ('Arial', 20, 'bold')
        labelfont = ('Arial', 50, 'bold')
        labelTitle = tkinter.Label(self, text="MMCS", font=labelfont)
        label_user = tkinter.Label(self, text="Welcome, " + get_user_name(get_logged_in_user()), font=label_font)
        add_edit_btn = tkinter.Button(self, text="Place Appointment", command=add_edit, pady=4, padx=4, width="20",
                                      height="5")
        student_list_btn = tkinter.Button(self, text="Check Status", command=lists, pady=4, padx=4, width="20",
                                          height="5")
        logout_btn = tkinter.Button(self, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
        exit_btn = tkinter.Button(self, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
        changePass_btn = tkinter.Button(self, text="Credential Settings", command=changePass, pady=4, padx=4,
                                        width="20",
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


class addAppointment_stu(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def search1():
            for i in tree.get_children():
                tree.delete(i)
            if len(search.get()) >= 1:
                if len(search_lecture(search.get())) == 0:
                    messagebox.showinfo("MMCS", "No match found.")
                else:
                    i = 1
                    for j in search_lecture(search.get()):
                        tree.insert('', 'end', text=str(i),
                                    values=(j[0], j[1], j[2], j[3]))
                        i = i + 1
            else:
                messagebox.showerror("MMCS", "Please enter the lecturer's name to search.")
            print("search")

        def confirm():
            curItem = tree.focus()
            # print(tree.item(curItem))
            values = tree.item(curItem)
            stu_ids = values['values']

            print("confirm")
            controller.show_frame("booking_student")

        def back():
            print("back")
            controller.show_frame("student_main")

        label_font_screen = ('Arial', 30)
        label = tkinter.Label(self, text="Place Appointment", font=label_font_screen)
        if platform.system() == "Windows":
            search = tkinter.Entry(self, bd=5, width=70)
            search_btn = tkinter.Button(self, text="Search", command=search1, pady=4, padx=4)
        else:
            search = tkinter.Entry(self, bd=5, width=50)
            search_btn = tkinter.Button(self, text="Search", command=search1, pady=4, padx=4)
        confirm_btn = tkinter.Button(self, text="Confirm", command=confirm, pady=4, padx=4, width="20", height="5",
                                     fg="green")
        back_btn = tkinter.Button(self, text="Back", command=back, pady=4, padx=4, width="20",
                                  height="5")
        tree = tker.Treeview(self)
        tree = tker.Treeview(self, columns=('Lecturer Name', 'Room Number', 'ID', 'Faculty'))

        tree.heading('#0', text='#')
        tree.heading('#1', text='Lecturer Name')
        tree.heading('#2', text='Room Number')
        tree.heading('#3', text='ID')
        tree.heading('#4', text='Faculty')

        tree.column('#0', width=40, anchor=tkinter.CENTER)
        tree.column('#1', width=400, anchor=tkinter.CENTER)
        tree.column('#2', width=100, anchor=tkinter.CENTER)
        tree.column('#3', width=100, anchor=tkinter.CENTER)
        tree.column('#4', width=100, anchor=tkinter.CENTER)

        def selectItem(a):
            curItem = tree.focus()
            # print(tree.item(curItem))
            values = tree.item(curItem)
            stu_ids = values['values']
            print(str(stu_ids[2]))  # output selected lec's id

        tree.bind('<Double-Button-1>', selectItem)

        if platform.system() == "Windows":
            label.place(x=220, y=20)
            search.place(x=150, y=90)
            search_btn.place(x=590, y=83)
            tree.place(x=95, y=130)
            confirm_btn.place(x=600, y=500)
            back_btn.place(x=10, y=500)
        else:
            label.place(x=270, y=20)
            search.place(x=150, y=80)
            search_btn.place(x=620, y=83)
            tree.place(x=95, y=130)
            confirm_btn.place(x=600, y=500)
            back_btn.place(x=10, y=500)


if __name__ == "__main__":
    MMCS_Auth()
    top.mainloop()
