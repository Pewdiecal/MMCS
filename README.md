# MMCS
Consultation software designed for student and lecturers use in mmu.
Here are the functions to communicate with the database.


function name : add_lec_time(user_id, lec_day, time_start, time_end, date, availability)
Info : To add lecturer's free and available time into database.
Arguments : user_id = lecturer's id, lec_day = lec's free day, time_start = lec's free starting time, time_end = lec's free end time, availability = lec's time slot whether ("Available" or "Unavailable").
Example : add_lec_time("MU12345", "Monday", "13", "14", "13/04/2018", "Available")


function name : add_bookings(user_id, book_day, book_time, book_time_start, book_time_end, book_reason, book_student, stu_id,
                 book_date, book_status, reason_cancel)
Info : To add the students bookings with the lecturers into database.
Arguments : user_id = lec's id that the student is booking with, book_day = student's booking day, book_time = student's booking time, book_time_start = student's booking starting time, book_time_end = student's booking ending time, book_reason = student's booking reason, book_student = student's name whos make the booking, stu_id = student's id, book_date = student's booking date, book_status = confirmation status from lecturer("Pending", "Confirmed", "Cancelled"), reason_cancel = lecturer's reason for cancelling the bookings.
Example : add_bookings("MU12345", "Monday", "13", "13", "15", "I want to see u because.....", "John", "1102273388",
                        "10/3/2018", "Pending", "")
                        
                        
function name : get_logged_in_user()
Info : To get the current logged in user from database and output the currently logged in user id.
Output : 1171182299 


function name : check_user_id(user_id)
Info : To check the user id and see if its in the database or not, if yes it will return True if not it will return False.
Output : True or False
Example : check_user_id("1134485566")


function name : get_user_name(user_id)
Info : To get the user's full name with the user id 
Arguments : user_id = Insert the the user id of the user to get their name.
Output : John Lim
Example : get_user_name("1129948855")


function name : get_user_faculty(user_id)
Info : To get the user's faculty with their user id.
Output : FCI or FAC or FCM or FOE or FOM
Example : get_user_faculty("MU112344")


function name : get_lec_room(user_id)
Info : To get the lecturer's room number with their Id.
Output : BR2009
Example : get_lec_room("MU123456")


function name : get_user_position(user_id)
Info : To determind wether the user is a lecturer or a student with their Id
Output : LEC or STU
Example : get_user_position("1192235566")


function name : get_lec_free_time(user_id)
Info : To get the lecturer's available time slot using lec's id.
Output : [('Monday', '13', '14', '13/09/2019', 'Available')]
Example : get_lec_free_time("MU1313131")


function name : get_all_stu_bookings(stu_id)
Info : To get the student's booked time with lecturers by using the student's id.
Output : [('Suhaini', 'FAC', 'BR434', 'mon', '13', '15', 'asdasdasdaasdda', 'Faris', '1191181100', '13/11/15', 'approved', None)]
Example : get_all_stu_bookings("1192284455")


function name : get_all_lec_bookings(lec_id)
Info : Get all the lecturer's booking from students using the lecturer's id.
Output : [('Nicholas', 'mon', '13', '13/11/15', 'approved', '1191181100')]
Example : get_all_lec_bookings("MU123456")


function name : get_stu_booking_details(stu_id)
Info : Get all the students bookings details like the student's name, faculty, and booking time for the lecturer's.
Output : [('Aik Seng', '1191181100', '13/11/15', '13', '15', 'FCM', 'The reason I want to see you ......')]
Example : get_stu_booking_details("1191181100")


function name : get_lec_booking_details(stu_id, lec_id)
Info : Get all the lecturer's details like the lecturer's name, faculty, booking time and room number using both the student id and lecturer's id.
Output : [('Suhaini', '13/11/15', '13', '15', 'approved', 'FAC', 'BR434', 'The reason I want to see you ......')]
Example : get_lec_booking_details("1171102288", "MU1344555")


function name : logout_user()
Info : To log the user out.


function name : test_users_insert()
Info : To register fake user with fake accounts.
