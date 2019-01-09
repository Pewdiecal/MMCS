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


def add_new_user(usr_name, usr_id, usr_fac, usr_room, usr_pass, usr_position):
    c.execute("""INSERT INTO user_credentials (user_id, user_pass, user_name, user_faculty, user_room, user_position)
               VALUES (""" + '"' + usr_id + '"' + """, """ + '"' + usr_pass + '"' + """, """ + '"' + usr_name + '"' + """, """ + '"' + usr_fac + '"' + """,""" +
              '"' + usr_room + '"' + """, """ + '"' + usr_position + '"' + """);""")
    conn.commit()


def validate_user(user_id, user_pass):
    c.execute("""SELECT count(user_id) FROM user_credentials WHERE user_id = """ + '"' + user_id + '"'
              + " AND user_pass = " + '"' + user_pass + '";')
    respond = c.fetchone()
    print("MMCS_DB_validate_user : ", respond[0])
    if respond[0] == 0:
        return False
    else:
        c.execute("""SELECT user_id FROM user_credentials WHERE user_id = """ + '"' + user_id + '"'
                  + " AND user_pass = " + '"' + user_pass + '";')
        id = c.fetchone()
        c.execute("""UPDATE user_credentials SET login_status = "Logged In" WHERE user_id = """ + '" ' + id[0] + ' ";')
        return True


def currentLoggedInUser():
    c.execute("""SELECT user_id FROM user_credentials WHERE login_status = "Logged In" """)
    respond = c.fetchone()
    print("MMCS_DB_currentLoggedIn : " + respond[0])
    return respond[0]


def add_lec_time(user_id, lec_day, time_start, time_end, date):
    c.execute(
        """INSERT INTO lec_available_time (user_id, lec_day, lec_time_start, lec_time_end, lec_date) VALUES (""" + '"' + user_id + '"' +
        "," + '"' + lec_day + '"' + "," + '"' + time_start + '"' + "," + '"' + time_end + '"' + "," + '"' + date + '"' + ");")
    conn.commit()


def add_bookings(user_id, book_day, book_time, book_time_start, book_time_end, book_reason, book_student, stu_id,
                 book_date, book_status, reason_cancel):
    c.execute(
        """INSERT INTO lec_bookings (user_id, book_day, book_time, book_time_start, book_time_end, book_reason, book_student, stu_id, book_date, book_status, reason_cancel) VALUES ("""
        + '"' + user_id + '"' + "," + '"' + book_day + '"' + "," + '"' + book_time + '"' + "," + '"' + book_time_start + '"' + ","
        + '"' + book_time_end + '"' + "," + '"' + book_reason + '"' + "," + '"' + book_student + '"' + "," + '"' + stu_id + '"' + ","
        + '"' + book_date + '"' + "," + '"' + book_status + '"' + "," + '"' + reason_cancel + '"' + ");")
    conn.commit()


c.execute("""CREATE TABLE IF NOT EXISTS lec_available_time(
            user_id VARCHAR(45) NOT NULL,
            lec_day VARCHAR(45) NOT NULL,
            lec_time_start VARCHAR(45) NOT NULL,
            lec_time_end VARCHAR(45) NOT NULL,
            lec_date DATE NOT NULL,
            PRIMARY KEY (user_id))
            """)

c.execute("""CREATE TABLE IF NOT EXISTS lec_bookings(
            user_id VARCHAR(45) NOT NULL,
            book_day VARCHAR(45) NOT NULL,
            book_time VARCHAR(45) NOT NULL,
            book_time_start VARCHAR(45) NOT NULL,
            book_time_end VARCHAR(45) NOT NULL,
            book_reason TEXT NOT NULL,
            book_student TEXT NOT NULL,
            stu_id VARCHAR(45) NOT NULL,
            book_date DATE NOT NULL,
            book_status VARCHAR NOT NULL,
            reason_cancel TEXT,
            PRIMARY KEY (user_id, stu_id))
            """)

conn.commit()


def logout():
    conn.close()
