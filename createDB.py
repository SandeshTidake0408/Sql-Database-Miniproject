import sqlite3 

def create_db():
    con = sqlite3.connect(database="rms.db")
    cursor = con.cursor()
    cursor.execute("create table if not exists course(cid integer primary key autoincrement,name text,duration text, charges text, description text)")
    con.commit()
    
create_db()