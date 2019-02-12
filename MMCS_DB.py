import sqlite3

conn = sqlite3.connect('mmcs.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_credentials(
            user_id VARCHAR(45) NOT NULL,
            user_pass VARCHAR(45) NOT NULL,
            user_name TEXT NOT NULL,
            user_faculty TEXT NOT NULL,
            user_room VARCHAR(45),
            user_position VARCHAR(45) NOT NULL,
            login_status VARCHAR(45),
            PRIMARY KEY (user_id));
            """)


c.execute("""CREATE TABLE IF NOT EXISTS lec_available_time(
            user_id VARCHAR(45) NOT NULL,
            lec_day VARCHAR(45) NOT NULL,
            lec_time_start VARCHAR(45) NOT NULL,
            lec_time_end VARCHAR(45) NOT NULL,
            lec_date DATE NOT NULL,
            time_availability TEXT NOT NULL);
            """)

c.execute("""CREATE TABLE IF NOT EXISTS lec_bookings(
            user_id VARCHAR(45) NOT NULL,
            book_day VARCHAR(45) NOT NULL,
            book_time_start VARCHAR(45) NOT NULL,
            book_time_end VARCHAR(45) NOT NULL,
            book_reason TEXT NOT NULL,
            book_student TEXT NOT NULL,
            stu_id VARCHAR(45) NOT NULL,
            book_date DATE NOT NULL,
            book_status VARCHAR NOT NULL,
            reason_cancel TEXT);
            """)


def add_new_user(usr_name, usr_id, usr_fac, usr_room, usr_pass, usr_position):
    c.execute("""INSERT INTO user_credentials (user_id, user_pass, user_name, user_faculty, user_room, user_position)
               VALUES (""" + '"' + usr_id + '"' + """, """ + '"' + usr_pass + '"' + """, """ + '"' + usr_name + '"'
              + """, """ + '"' + usr_fac + '"' + """,""" + 'UPPER("' + usr_room + '")' + """, """ + '"'
              + usr_position + '"' + """);""")
    conn.commit()


def validate_user(user_id, user_pass):
    c.execute("""UPDATE user_credentials SET login_status = "Logged Out"; """)
    c.execute("""SELECT count(user_id) FROM user_credentials WHERE user_id = """ + '"' + user_id + '"'
              + " AND user_pass = " + '"' + user_pass + '";')
    respond = c.fetchone()
    print("MMCS_DB_validate_user : ", respond[0])
    if respond[0] == 0:

        return False
    else:
        c.execute("""SELECT user_id FROM user_credentials WHERE user_id = """ + '"' + user_id + '"'
                  + " AND user_pass = " + '"' + user_pass + '";')
        userid = c.fetchone()
        print("correct")
        c.execute("""UPDATE user_credentials SET login_status = "Logged In" WHERE user_id = """ + '"' + userid[0] + '";')
        conn.commit()
        return True


def add_lec_time(user_id, lec_day, time_start, time_end, date, availability):
    c.execute(
        """INSERT INTO lec_available_time (user_id, lec_day, lec_time_start, lec_time_end, lec_date, time_availability) 
        VALUES (""" + '"' + user_id + '"' + "," + '"' + lec_day + '"' + "," + '"' + time_start + '"' + ","
        + '"' + time_end + '"' + "," + '"' + date + '"' + "," + '"' + availability + '"' + ");")
    conn.commit()


def add_bookings(user_id, book_day, book_time, book_time_start, book_time_end, book_reason, book_student, stu_id,
                 book_date, book_status, reason_cancel):
    c.execute(
        """INSERT INTO lec_bookings (user_id, book_day, book_time, book_time_start, book_time_end, book_reason, 
        book_student, stu_id, book_date, book_status, reason_cancel) VALUES (""" + '"' + user_id + '"' + ","
        + '"' + book_day + '"' + "," + '"' + book_time + '"' + "," + '"' + book_time_start + '"' + ","
        + '"' + book_time_end + '"' + "," + '"' + book_reason + '"' + "," + '"' + book_student + '"' + ","
        + '"' + stu_id + '"' + "," + '"' + book_date + '"' + "," + '"' + book_status + '"' + ","
        + '"' + reason_cancel + '"' + ");")
    conn.commit()


def update_approval_status(stu_id, user_id, date, boolean):
    if boolean:
        c.execute("""UPDATE lec_bookings SET book_status = "Approved" WHERE stu_id = """ + '"' + str(stu_id) + '"'
                  + " AND user_id = " + '"' + str(user_id) + '"' + " AND book_date = " + '"' + date + '";')
    else:
        c.execute("""UPDATE lec_bookings SET book_status = "Rejected" WHERE stu_id = """ + '"' + str(stu_id) + '"'
                  + " AND user_id = " + '"' + str(user_id) + '"' + " AND book_date = " + '"' + date + '";')
    conn.commit()


def update_user_password(user_id, old_pass, new_pass):
    c.execute("""SELECT count(user_pass) FROM user_credentials WHERE user_id = """ + '"' + user_id + '"'
              + "AND user_pass = " + '"' + old_pass + '";')
    respond = c.fetchone()
    if respond[0] == 1:
        c.execute("""UPDATE user_credentials SET user_pass = """ + '"' + new_pass + '"' + "WHERE user_id = "
                  + '"' + user_id + '";')
        conn.commit()
        return True
    else:
        return False


def get_logged_in_user():
    c.execute("""SELECT count(user_id) FROM user_credentials WHERE login_status = "Logged In"; """)
    respond = c.fetchone()
    if respond[0] == 0:
        return False
    else:
        c.execute("""SELECT user_id FROM user_credentials WHERE login_status = "Logged In"; """)
        respond = c.fetchone()
        print("MMCS_DB_currentLoggedIn : " + respond[0])
        return respond[0]


def check_user_id(user_id):
    c.execute("""SELECT count(user_id) FROM user_credentials WHERE user_id = """ + '"' + user_id + '";')
    respond = c.fetchone()
    if respond[0] >= 1:
        return False
    else:
        return True


def get_user_name(user_id):
    c.execute("""SELECT user_name FROM user_credentials WHERE user_id = """ + '"' + user_id + '" OR user_name = ' + '"'
                        + user_id + '";')
    respond = c.fetchone()
    print("MMCS_DB_User_Name : " + respond[0])
    return respond[0]


def get_user_faculty(user_id):
    c.execute("""SELECT user_faculty FROM user_credentials WHERE user_id = """ + '"' + user_id + '";')
    respond = c.fetchone()
    print("MMCS_DB_User_Faculty : " + respond[0])
    return respond[0]


def get_lec_room(user_id):
    c.execute("""SELECT user_room FROM user_credentials WHERE user_id = """ + '"' + user_id + '";')
    respond = c.fetchone()
    print("MMCS_DB_User_Room : " + respond[0])
    return respond[0]


def get_user_position(user_id):
    c.execute("""SELECT user_position FROM user_credentials WHERE user_id = """ + '"' + user_id + '";')
    respond = c.fetchone()
    print("MMCS_DB_User_Position : " + respond[0])
    return respond[0]


def get_lec_free_time(user_id):
    c.execute("""SELECT lec_day, lec_time_start, lec_time_end, lec_date, time_availability 
                FROM lec_available_time WHERE user_id = """ + '"' + user_id + '" AND time_availability = "Available";')
    respond = c.fetchall()
    for i in respond:
        print("MMCS_DB_Lec_Free_Time : ", i)
    return respond


def get_all_stu_bookings(stu_id):
    c.execute("""SELECT user_credentials.user_name, user_credentials.user_faculty, user_credentials.user_room, 
                lec_bookings.book_day, lec_bookings.book_time_start, lec_bookings.book_time_end, lec_bookings.book_reason,
                lec_bookings.book_student, lec_bookings.stu_id, lec_bookings.book_date, lec_bookings.book_status,
                lec_bookings.reason_cancel FROM user_credentials INNER JOIN lec_bookings ON user_credentials.user_id = 
                lec_bookings.user_id WHERE lec_bookings.stu_id = """ + '"' + stu_id + '";')
    respond = c.fetchall()
    print("MMCS_DB_STU_BOOK : " + str(respond))
    return respond


def get_all_lec_bookings(lec_id):
    c.execute("""SELECT lec_bookings.book_student, lec_bookings.book_day, lec_bookings.book_time_start, 
                        lec_bookings.book_date, lec_bookings.book_status, lec_bookings.stu_id
                        FROM lec_bookings WHERE lec_bookings.user_id = """ + '"' + lec_id + '";')
    respond = c.fetchall()
    print("MMCS_DB_LEC_BOOK : " + str(respond))
    return respond


def get_stu_booking_details(stu_id):  # for lec module
    c.execute("""SELECT user_credentials.user_name, lec_bookings.stu_id, lec_bookings.book_date, 
                        lec_bookings.book_time_start, lec_bookings.book_time_end,
                        user_credentials.user_faculty, lec_bookings.book_reason 
                        FROM user_credentials INNER JOIN lec_bookings 
                        ON user_credentials.user_id = lec_bookings.stu_id 
                        WHERE lec_bookings.stu_id = """ + '"' + stu_id + '";')
    respond = c.fetchall()
    print("MMCS_DB_STU_BOOK_DETAILS : " + str(respond))
    return respond


def get_lec_booking_details(stu_id, lec_id):  # for stu module
    c.execute("""SELECT user_credentials.user_name, lec_bookings.book_date, 
                        lec_bookings.book_time_start, lec_bookings.book_time_end,
                        lec_bookings.book_status, user_credentials.user_faculty, 
                        user_credentials.user_room, lec_bookings.book_reason
                        FROM user_credentials INNER JOIN lec_bookings 
                        ON user_credentials.user_id = lec_bookings.user_id 
                        WHERE lec_bookings.stu_id = """ + '"' + stu_id + '"' + " AND " + "lec_bookings.user_id = " +
                        '"' + lec_id + '";')
    respond = c.fetchall()
    print("MMCS_DB_LEC_BOOK_DETAILS : " + str(respond))
    return respond


def get_user_reason(stu_id, lec_id):
    c.execute("""SELECT book_reason FROM lec_bookings WHERE user_id = """ + '"' + lec_id + '" AND stu_id = ' + '"'
                        + stu_id + '";')
    respond = c.fetchone()
    return respond[0]


def search_lecture(lec_name):
    c.execute("""SELECT user_name, user_room, user_id, user_faculty FROM user_credentials WHERE user_name LIKE """
              + "'%" + lec_name + "%'" + " AND user_position = " + '"' + "LEC" + '";')
    respond = c.fetchall()
    print("MMCS_DB_SEARCHED_RES: " + str(respond))
    return respond


def logout_user():
    c.execute("""UPDATE user_credentials SET login_status = "Logged Out" WHERE login_status = "Logged In" """)
    conn.commit()
    print("Logged Out Success")


conn.commit()


