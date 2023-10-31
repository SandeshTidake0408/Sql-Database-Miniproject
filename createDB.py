import sqlite3


def create_db():
    con = sqlite3.connect(database="rms.db")
    cursor = con.cursor()
    cursor.execute(
        "create table if not exists course(cid integer primary key autoincrement,name text,duration text, charges text, description text)")
    con.commit()
    cursor.execute("create table if not exists student(roll integer primary key autoincrement, name text, email text, gender text, dob text, contact text,admission text, course text, state text, city text, pincode text, address text)")
    con.commit()
    cursor.execute(
        "create table if not exists result(rid integer primary key autoincrement,roll text, name text, course text, marks_ob text,full_marks text, per text)")
    con.commit()
    con.close()


create_db()
