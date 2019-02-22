import tkinter
import os
import platform
import sqlite3
from tkinter import messagebox
from tkinter import ttk as tker
from MMCS_DB import *
from datetime import date
import time
import datetime
import calendar

top = tkinter.Tk()
top.geometry("900x600")
top.title("Multimedia Consultation Software")
top.resizable(False, False)
photo = tkinter.PhotoImage(file="mmu.gif")


def dateConverterLEC(book_day):
    dateToday = date.today()
    dayToday = int(dateToday.strftime("%d"))
    monthToday = int(dateToday.strftime("%m"))
    yearToday = int(dateToday.strftime("%Y"))
    dnameToday = dateToday.strftime("%A")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("dnameToday : " + dnameToday)

    i = dayToday
    while True:
        i = i + 1
        maxDay = calendar.monthrange(yearToday, monthToday)
        if i > maxDay[1]:  # check for 30,28,29,31 days
            i = 1
            monthToday = monthToday + 1
        if monthToday > 12:  # check for max month for that year
            monthToday = 1
            yearToday = yearToday + 1

        dayDate = date(yearToday, monthToday, i)
        dayIndex = days.index(book_day)

        if dayDate.weekday() == dayIndex:
            print("Date for " + book_day + " is " + str(dayDate))
            return str(dayDate)


def MMCS_Auth():
    def AuthFunc():
        print("login")
        if len(username.get()) > 1 and len(password.get()) > 1:
            if str(username.get()).isalnum() and str(password.get()).isalnum():
                if validate_user(username.get(), password.get()):
                    if get_user_position(get_logged_in_user()) == "LEC":
                        for widget in top.winfo_children():
                            widget.destroy()
                        lecturer_main()
                    else:
                        for widget in top.winfo_children():
                            widget.destroy()
                        student_main()
                else:
                    messagebox.showinfo("Authentication", "Username or password incorrect.")
            else:
                messagebox.showerror("Error", "Only alphanum char is allowed.")

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


def Add_Edit_Func():  # Lec module
    day_array = []
    time_start_array = []
    time_end_array = []

    def add():
        if len(dayList_box.curselection()) > 0:
            if len(hrs_entry.get()) > 0 and len(min_entry.get()) > 0 and len(hrs2_entry.get()) > 0 and len(
                    mins2_entry.get()) > 0:
                print(str(hrs_entry.get()).isdigit(), str(hrs2_entry.get()).isdigit(), str(min_entry.get()).isdigit(),
                      str(mins2_entry.get()).isdigit())
                if str(hrs_entry.get()).isdigit() and str(hrs2_entry.get()).isdigit() and str(
                        min_entry.get()).isdigit() and str(mins2_entry.get()).isdigit():
                    if (int(hrs_entry.get()) < 24) and (int(min_entry.get()) < 60) and (
                            int(hrs2_entry.get()) < 24) and (int(mins2_entry.get()) < 60):
                        day = dayList_box.get(dayList_box.curselection())
                        try:
                            time_start = datetime.timedelta(hours=int(hrs_entry.get()), minutes=int(min_entry.get()))
                            time_end = datetime.timedelta(hours=int(hrs2_entry.get()), minutes=int(mins2_entry.get()))
                            Tduration = time.strptime(str(time_end - time_start), "%H:%M:%S")
                            if len(day_array) == 0:
                                day_array.append(day)
                                time_start_array.append(str(time_start))
                                time_end_array.append(str(time_end))
                                tree.insert("", 'end', text=str(len(tree.get_children()) + 1),
                                            values=(day, str(time_start), str(time_end),
                                                    str(Tduration[3]) + " HRS " + str(Tduration[4]) + " MIN"))
                            elif len(day_array) > 0:
                                i = 0
                                while i <= (len(day_array) - 1):
                                    if day_array[i] == day and time_start_array[i] == str(time_start) and \
                                            time_end_array[i] == str(
                                            time_end):
                                        print(i)
                                        messagebox.showinfo("MMCS", "The time slot is already existed.")
                                        break
                                    elif i == (len(day_array) - 1):
                                        day_array.append(day)
                                        time_start_array.append(str(time_start))
                                        time_end_array.append(str(time_end))
                                        tree.insert("", 'end', text=str(len(tree.get_children()) + 1),
                                                    values=(day, str(time_start), str(time_end),
                                                            str(Tduration[3]) + " HRS " + str(Tduration[4]) + " MIN"))
                                        break
                                    i = i + 1
                        except ValueError as error:
                            messagebox.showerror("Error", "Please set a valid time.")
                    else:
                        messagebox.showerror("Error", "Time input invalid.")
                else:
                    messagebox.showerror("Error", "Only digit inputs are allowed")
            else:
                messagebox.showerror("Error", "Please complete your time slot time.")
        else:
            messagebox.showerror("Error", "Please select your day for your time slot.")

        print("add")

    def remove():
        curItem = tree.focus()
        # print(tree.item(curItem))
        indexItem = tree.index(curItem)
        if len(curItem) !=0:
            values = tree.item(curItem)
            stu_ids = values['values']
            print(values)
            day_array.remove(stu_ids[0])
            time_start_array.remove(stu_ids[1])
            time_end_array.remove(stu_ids[2])
            remove_bookings(get_logged_in_user(), stu_ids[0], stu_ids[1], stu_ids[2])
            tree.delete(curItem)
        else:
            messagebox.showerror("Error", "Please select a timeslot to remove.")
        print("remove")

    def confirm():
        print("confirm")
        if len(day_array) == 0:
            for widget in top.winfo_children():
                widget.destroy()
            lecturer_main()
        else:
            messagebox.showinfo("MMCS", "Time slot added.")
            for i in range(len(day_array)):
                print(day_array)
                add_lec_time(get_logged_in_user(), day_array[i], time_start_array[i], time_end_array[i],
                             dateConverterLEC(day_array[i]), "Available")
                for widget in top.winfo_children():
                    widget.destroy()
                lecturer_main()

    def back():
        print("back")
        for widget in top.winfo_children():
            widget.destroy()
        lecturer_main()

    label_font_screen = ('Arial', 30)
    label = tkinter.Label(top, text="Schedule Availability", font=label_font_screen)
    select_day_label = tkinter.Label(top, text="Select Day")
    select_time_label = tkinter.Label(top, text="Select Time (24Hrs format)")
    dayList_box = tkinter.Listbox(top)
    dayList_box.insert(1, "Monday")
    dayList_box.insert(2, "Tuesday")
    dayList_box.insert(3, "Wednesday")
    dayList_box.insert(4, "Thursday")
    dayList_box.insert(5, "Friday")
    hrs_label = tkinter.Label(top, text="Hrs")
    hrs_entry = tkinter.Entry(top, bd=5, width=5)
    min_label = tkinter.Label(top, text="Mins")
    min_entry = tkinter.Entry(top, bd=5, width=5)
    hrs2_label = tkinter.Label(top, text="Hrs")
    hrs2_entry = tkinter.Entry(top, bd=5, width=5)
    mins2_label = tkinter.Label(top, text="Mins")
    mins2_entry = tkinter.Entry(top, bd=5, width=5)
    start_label = tkinter.Label(top, text="Start")
    end_label = tkinter.Label(top, text="End")
    to_label = tkinter.Label(top, text="To")
    add_btn = tkinter.Button(top, text="Add Time", command=add, pady=4, padx=4)
    remove_btn = tkinter.Button(top, text="Remove Time", command=remove, pady=4, padx=4)
    confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                                 height="5", fg="green")
    back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                              height="5")

    tree = tker.Treeview(top)
    tree = tker.Treeview(top, columns=('Day', 'Time Start', 'Time End', 'Duration'))

    tree.heading('#0', text='#')
    tree.heading('#1', text='Day')
    tree.heading('#2', text='Time Start')
    tree.heading('#3', text='Time End')
    tree.heading('#4', text='Duration')

    tree.column('#0', width=40, anchor=tkinter.CENTER)
    tree.column('#1', width=200, anchor=tkinter.CENTER)
    tree.column('#2', width=100, anchor=tkinter.CENTER)
    tree.column('#3', width=100, anchor=tkinter.CENTER)
    tree.column('#4', width=200, anchor=tkinter.CENTER)

    for j in range(len(get_lec_time_slots(get_logged_in_user()))):
        array_data = get_lec_time_slots(get_logged_in_user())[j]
        time_start = time.strptime(array_data[1], "%H:%M:%S")
        time_end = time.strptime(array_data[2], "%H:%M:%S")
        time_stamp_start = datetime.timedelta(hours=int(time_start[3]), minutes=int(time_start[4]))
        time_stamp_end = datetime.timedelta(hours=int(time_end[3]), minutes=int(time_end[4]))
        Tduration = time.strptime(str(time_stamp_end - time_stamp_start), "%H:%M:%S")
        day_array.append(array_data[0])
        time_start_array.append(str(time_stamp_start))
        time_end_array.append(str(time_stamp_end))
        tree.insert("", 'end', text=str(j + 1),
                    values=(day_array[j], str(time_start_array[j]), str(time_end_array[j]),
                            str(Tduration[3]) + " HRS " + str(Tduration[4]) + " MINS"))

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
        tree.place(x=130, y=270)

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


def student_appointment_list():  # stu module

    def back():
        print("back")
        for widget in top.winfo_children():
            widget.destroy()
        student_main()

    label_font_screen = ('Arial', 30)
    label = tkinter.Label(top, text="Student Appointment Status List", font=label_font_screen)
    labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
    labelName = tkinter.Label(top, text="Lecturer Name: ")
    labelTime = tkinter.Label(top, text="Consultation Time: ")
    labelDate = tkinter.Label(top, text="Date: ")
    labelFaculty = tkinter.Label(top, text="Faculty: ")
    labelRoom = tkinter.Label(top, text="Room Number: ")
    labelReason = tkinter.Label(top, text="Cancellation Reason: ")
    labelStatus = tkinter.Label(top, text="Status: ")
    back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                              height="5")

    tree = tker.Treeview(top)
    tree = tker.Treeview(top, columns=('Lecturer Name', 'Day', 'Time', 'ID', 'Status'))

    tree.heading('#0', text='#')
    tree.heading('#1', text='Lecturer Name')
    tree.heading('#2', text='Day')
    tree.heading('#3', text='Time')
    tree.heading('#4', text='ID')
    tree.heading('#5', text='Status')

    tree.column('#0', width=40, anchor=tkinter.CENTER)
    tree.column('#1', width=300, anchor=tkinter.CENTER)
    tree.column('#2', width=100, anchor=tkinter.CENTER)
    tree.column('#3', width=200, anchor=tkinter.CENTER)
    tree.column('#4', width=100, anchor=tkinter.CENTER)
    tree.column('#5', width=100, anchor=tkinter.CENTER)

    def selectItem(a):
        curItem = tree.focus()
        # print(tree.item(curItem))
        indexItem = tree.index(curItem)
        values = tree.item(curItem)
        stu_ids = values['values']
        array_data = get_all_stu_bookings(get_logged_in_user())[indexItem]
        labelName.config(text="Lecturer Name: " + stu_ids[0])
        labelTime.config(text="Consultation Time: " + stu_ids[2])
        print(array_data)
        labelDate.config(text="Date: " + array_data[10])
        labelFaculty.config(text="Faculty: " + array_data[1])
        labelRoom.config(text="Room Number: " + array_data[2])
        labelReason.config(text="Cancellation Reason: " + array_data[12])
        labelStatus.config(text="Status: " + stu_ids[4])

    tree.bind('<Double-Button-1>', selectItem)
    for j in range(len(get_all_stu_bookings(get_logged_in_user()))):
        array_data = get_all_stu_bookings(get_logged_in_user())[j]
        tree.insert("", 'end', text=str(j + 1), values=(array_data[0], array_data[4], array_data[5] + " HRS " + "to " +
                                                        array_data[6] + " HRS", array_data[3], array_data[11]))

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


def booking_student(selectedID):
    def confirm():
        print("confirm")
        curItem = tree.focus()
        indexItem = tree.index(curItem)
        values = tree.item(curItem)
        book_day = values['values']
        if len(book_day) > 0:
            if len(reason_text.get("1.0", 'end')) >= 10:
                array_time = get_lec_free_time(selectedID)[indexItem]
                str(reason_text.get("1.0", 'end')).replace('"', "")
                add_bookings(selectedID, book_day[0], array_time[1], array_time[2], reason_text.get("1.0", 'end'),
                             get_user_name(get_logged_in_user()), get_logged_in_user(), array_time[3],
                             "Pending", "NULL")
                messagebox.showinfo("MMCS", "Appointment has been made.")
                for widget in top.winfo_children():
                    widget.destroy()
                student_main()
            else:
                messagebox.showerror("MMCS", "Please enter your reason.")
        else:
            messagebox.showerror("MMCS", "Please select a time slot.")

    def back():
        print("back")
        for widget in top.winfo_children():
            widget.destroy()
        MMCS_Student_Search()

    label_font_screen = ('Arial', 30)
    label = tkinter.Label(top, text="Booking Schedule", font=label_font_screen)
    list_label = tkinter.Label(top, text="Select your time")
    reason_label = tkinter.Label(top, text="Reason: ")
    if platform.system() == "Windows":
        reason_text = tkinter.Text(top, width=73, height=8, highlightbackground="grey")
    else:
        reason_text = tkinter.Text(top, width=80, height=8, highlightbackground="grey")

    confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20",
                                 height="2", fg="green")
    back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                              height="2")

    tree = tker.Treeview(top)
    tree = tker.Treeview(top, columns=('Day', 'Time', 'Date', 'Duration'))

    tree.heading('#0', text='#')
    tree.heading('#1', text='Day')
    tree.heading('#2', text='Time')
    tree.heading('#3', text='Date')
    tree.heading('#4', text='Duration')

    tree.column('#0', width="40", anchor=tkinter.CENTER)
    tree.column('#1', width=200, anchor=tkinter.CENTER)
    tree.column('#2', width=300, anchor=tkinter.CENTER)
    tree.column('#3', width=100, anchor=tkinter.CENTER)
    tree.column('#4', width=100, anchor=tkinter.CENTER)

    for j in range(len(get_lec_free_time(selectedID))):
        full_array = (get_lec_free_time(selectedID))[j]
        time_start = time.strptime(full_array[1], "%H:%M:%S")
        time_end = time.strptime(full_array[2], "%H:%M:%S")
        time_stamp_start = datetime.timedelta(hours=int(time_start[3]), minutes=int(time_start[4]))
        time_stamp_end = datetime.timedelta(hours=int(time_end[3]), minutes=int(time_end[4]))
        Tduration = time.strptime(str(time_stamp_end - time_stamp_start), "%H:%M:%S")
        tree.insert("", 'end', text=str(j + 1),
                    values=(full_array[0], str(time_stamp_start) + " TO " + str(time_stamp_end), full_array[3],
                            str(Tduration[3]) + " HRS " + str(Tduration[4]) + " MIN"))

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


def password_change():
    def back():
        if get_user_position(get_logged_in_user()) == "LEC":
            for widget in top.winfo_children():
                widget.destroy()
            lecturer_main()
        else:
            for widget in top.winfo_children():
                widget.destroy()
            student_main()
        print("back")

    def confirm():
        if oldPass_entry.get() != "" and newPass_entry.get() != "" and confirmPass_entry.get() != "":
            if str(oldPass_entry.get()).isalnum() and str(newPass_entry.get()):
                if len(newPass_entry.get()) >= 8:
                    if newPass_entry.get() == confirmPass_entry.get():
                        if update_user_password(get_logged_in_user(), oldPass_entry.get(), newPass_entry.get()):
                            messagebox.showinfo("Credential Settings", "Password Changed.")
                            oldPass_entry.delete(0, 'end')
                            newPass_entry.delete(0, 'end')
                            confirmPass_entry.delete(0, 'end')
                            if get_user_position(get_logged_in_user()) == "LEC":
                                for widget in top.winfo_children():
                                    widget.destroy()
                                lecturer_main()
                            else:
                                for widget in top.winfo_children():
                                    widget.destroy()
                                student_main()
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


def lecturer_main():
    def add_edit():
        print("add/edit")
        for widget in top.winfo_children():
            widget.destroy()
        Add_Edit_Func()

    def lists():
        print("student list")
        for widget in top.winfo_children():
            widget.destroy()
        listStudent_lecturer()

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
        for widget in top.winfo_children():
            widget.destroy()
        password_change()

    labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
    label_font = ('Arial', 20, 'bold')
    labelfont = ('Arial', 50, 'bold')
    labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)

    label_user = tkinter.Label(top, text="Welcome, " + get_user_name(get_logged_in_user()), font=label_font)
    add_edit_btn = tkinter.Button(top, text="Add/Edit Schedule", command=add_edit, pady=4, padx=4, width="20",
                                  height="5")
    student_list_btn = tkinter.Button(top, text="List Of Students", command=lists, pady=4, padx=4, width="20",
                                      height="5")
    logout_btn = tkinter.Button(top, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
    exit_btn = tkinter.Button(top, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
    changePass_btn = tkinter.Button(top, text="Credential Settings", command=changePass, pady=4, padx=4,
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


def listStudent_lecturer():
    def approve():
        curItem = tree.focus()
        values = tree.item(curItem)
        stu_ids = values['values']
        reason = ""
        try:
            update_approval_status(stu_ids[3], get_logged_in_user(), stu_ids[1], stu_ids[2], True)
            update_time_slot_stat(stu_ids[2], stu_ids[1], get_logged_in_user(), True)
            update_reason_cancel(stu_ids[3], get_logged_in_user(), stu_ids[1], reason)
            print("TREE :", tree.get_children())
            for i in tree.get_children():
                tree.delete(i)
            for j in range(len(get_all_lec_bookings(get_logged_in_user()))):
                full_array = (get_all_lec_bookings(get_logged_in_user()))[j]
                tree.insert("", 'end', text=str(j + 1),
                            values=(full_array[0], full_array[3], full_array[2], full_array[5], full_array[4]))

            print("approve")
        except IndexError as error:
            messagebox.showerror("MMCS", "Please select a student to Approve.")

    def cancel():
        curItem = tree.focus()
        values = tree.item(curItem)
        stu_ids = values['values']
        

        class Reason(tkinter.Tk):
            def __init__(self):
                tkinter.Tk.__init__(self)
                self.geometry("500x50")
                self.title("Please enter reason for cancelling")
                self.entry = tkinter.Entry(self)
                self.button = tkinter.Button(self, text="Ok", command=self.on_button)
                self.entry.place(width=500, height=25)
                self.button.place(width=100, height=25, x=200, y=25)
                self.wait_window()

            def on_button(self):
                update_reason_cancel(stu_ids[3], get_logged_in_user(), stu_ids[1], self.entry.get())
                self.destroy()

        if curItem != "":
            try:
                cancel_btn.config(state="disabled")
                back_btn.config(state="disabled")
                approve_btn.config(state="disabled")
                Reason()
                update_approval_status(stu_ids[3], get_logged_in_user(), stu_ids[1], stu_ids[2], False)
                update_time_slot_stat(stu_ids[2], stu_ids[1], get_logged_in_user(), False)
                for i in tree.get_children():
                    tree.delete(i)
                for j in range(len(get_all_lec_bookings(get_logged_in_user()))):
                    full_array = (get_all_lec_bookings(get_logged_in_user()))[j]
                    tree.insert("", 'end', text=str(j + 1),
                                values=(full_array[0], full_array[3], full_array[2], full_array[5], full_array[4]))
                print("Cancel")
            except IndexError as error:
                messagebox.showerror("MMCS", "Please select a student to Cancel.")
            cancel_btn.config(state="normal")
            back_btn.config(state="normal")
            approve_btn.config(state="normal")
        else:
            messagebox.showerror("MMCS", "Please select a student to Cancel.")

    def back():
        print("back")
        for widget in top.winfo_children():
            widget.destroy()
        lecturer_main()
    label_font_screen = ('Arial', 30)
    label = tkinter.Label(top, text="Student Appointment List", font=label_font_screen)
    labelDetails = tkinter.Label(top, text="Appointment Details", font=label_font_screen)
    labelName = tkinter.Label(top, text="Student Name: ")
    labelID = tkinter.Label(top, text="ID: ")
    labelTime = tkinter.Label(top, text="Consultation Time: ")
    labelDate = tkinter.Label(top, text="Date: ")
    labelReason = tkinter.Label(top, text="Reason: ")
    labelFaculty = tkinter.Label(top, text="Faculty: ")
    approve_btn = tkinter.Button(top, text="Confirm Appointment", command=approve, pady=4, padx=4, width="20",
                                 height="2", fg="green")
    cancel_btn = tkinter.Button(top, text="Cancel Appointment", command=cancel, pady=4, padx=4, width="20",
                                height="2", fg="red")
    back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                              height="2")
    tree = tker.Treeview(top)
    tree = tker.Treeview(top, columns=('Name', 'Date', 'Time', 'ID', 'Status'))

    tree.heading('#0', text='#')
    tree.heading('#1', text='Name')
    tree.heading('#2', text='Date')
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
        tree.insert("", 'end', text=str(j + 1),
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
                if str(fullname_entry.get()).isalpha():
                    if str(userID_entry.get()).isalnum():
                        if str(room_entry.get()).isalnum():
                            if str(pass_entry.get()).isalnum():
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
                            else:
                                messagebox.showerror("Error", "Only alpha and numeric char are allowed for password.")
                        else:
                            messagebox.showerror("Error", "Only alpha and numeric char are allowed for room number.")
                    else:
                        messagebox.showerror("Error", "Only alpha and numeric char are allowed for user ID.")
                else:
                    messagebox.showerror("Error", "Only alphabetical char are allowed for name.")
        elif var.get() == "STU":

            if len(fullname_entry.get()) >= 1 or len(userID_entry.get()) >= 1 or len(var_faculty.get()) >= 1:
                if str(fullname_entry.get()).isalpha():
                    if str(userID_entry.get()).isalnum():
                        if str(pass_entry.get()).isalnum():
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
                            messagebox.showerror("Error", "Only alpha and numeric char are allowed for password.")
                    else:
                        messagebox.showerror("Error", "Only alpha and numeric char are allowed for user ID.")
                else:
                    messagebox.showerror("Error", "Only alphabetical char are allowed for name.")
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


def student_main():
    def add_edit():
        print("place appointment")
        for widget in top.winfo_children():
            widget.destroy()
        MMCS_Student_Search()

    def lists():
        print("student list")
        for widget in top.winfo_children():
            widget.destroy()
        student_appointment_list()

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
        for widget in top.winfo_children():
            widget.destroy()
        password_change()

    labelPhoto = tkinter.Label(top, image=photo, width="100", height="100")
    label_font = ('Arial', 20, 'bold')
    labelfont = ('Arial', 50, 'bold')
    labelTitle = tkinter.Label(top, text="MMCS", font=labelfont)
    label_user = tkinter.Label(top, text="Welcome, " + get_user_name(get_logged_in_user()), font=label_font)
    add_edit_btn = tkinter.Button(top, text="Place Appointment", command=add_edit, pady=4, padx=4, width="20",
                                  height="5")
    student_list_btn = tkinter.Button(top, text="Check Status", command=lists, pady=4, padx=4, width="20",
                                      height="5")
    logout_btn = tkinter.Button(top, text="Logout", command=logout, pady=4, padx=4, width="20", height="5")
    exit_btn = tkinter.Button(top, text="Exit", command=exit, pady=4, padx=4, width="20", height="5")
    changePass_btn = tkinter.Button(top, text="Credential Settings", command=changePass, pady=4, padx=4,
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


def MMCS_Student_Search():
    def search1():
        try:
            for i in tree.get_children():
                tree.delete(i)
            if str(search.get()).isalpha():
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
            else:
                messagebox.showerror("MMCS", "Only alphabetic are allowed.")

        except sqlite3.OperationalError as error:
            messagebox.showerror("MMCS", "SUSPECIOUS INPUT FOUND PLEASE DONT DO THAT.")
        print("search")

    def confirm():
        curItem = tree.focus()
        if len(curItem) > 0: 
            values = tree.item(curItem)
            lec_id = values['values']
            print("confirm")
            if len(get_lec_free_time(str(lec_id[2]))) <= 0:
                messagebox.showinfo("MMCS", "This lecturer is unavailable for consultation for now. "
                                            "Please select a different lecturer.")
            else:
                for widget in top.winfo_children():
                    widget.destroy()
                booking_student(str(lec_id[2]))
        else:
            messagebox.showerror("Error", "No lecturer selected.")

    def back():
        print("back")
        for widget in top.winfo_children():
            widget.destroy()
        student_main()

    label_font_screen = ('Arial', 30)
    label = tkinter.Label(top, text="Place Appointment", font=label_font_screen)
    if platform.system() == "Windows":
        search = tkinter.Entry(top, bd=5, width=70)
        search_btn = tkinter.Button(top, text="Search", command=search1, pady=4, padx=4)
    else:
        search = tkinter.Entry(top, bd=5, width=50)
        search_btn = tkinter.Button(top, text="Search", command=search1, pady=4, padx=4)
    confirm_btn = tkinter.Button(top, text="Confirm", command=confirm, pady=4, padx=4, width="20", height="5",
                                 fg="green")
    back_btn = tkinter.Button(top, text="Back", command=back, pady=4, padx=4, width="20",
                              height="5")
    tree = tker.Treeview(top)
    tree = tker.Treeview(top, columns=('Lecturer Name', 'Room Number', 'ID', 'Faculty'))

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
        label.place(x=250, y=20)
        search.place(x=180, y=90)
        search_btn.place(x=615, y=83)
        tree.place(x=95, y=130)
        confirm_btn.place(x=700, y=500)
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
