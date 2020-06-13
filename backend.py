import sqlite3
import pandas as pd

def connect():
    conn=sqlite3.connect("To_Do.db")  # Database Creation
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Task_manager1 (id INTEGER PRIMARY KEY, Date text, Task_title text, Task_Detail text, Status text)")
    conn.commit()
    conn.close()

def insert(Date,Task_title, Task_Detail,Status):
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Task_manager1 VALUES (NULL,?,?,?,?)",(Date,Task_title, Task_Detail,Status))
    conn.commit()
    conn.close()    


def view_for_excel_generation():
    conn=sqlite3.connect("To_Do.db")
    df = pd.read_sql_query("SELECT * FROM Task_manager1", conn)
    return df

def view():
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Task_manager1")
    rows=cur.fetchall()
    conn.close()
    return rows

def view_With_date_only(date_only):
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Task_manager1 WHERE Date= ?", (date_only,))
    rows=cur.fetchall()
    conn.close()
    return rows

def view_With_filter(date_only):
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("SELECT Task_title, Status FROM Task_manager1 WHERE Date= ?", (date_only,))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(serial_num):  # Deleting ith unique id
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Task_manager1 WHERE id=?",(serial_num,))
    conn.commit()
    conn.close()

def update(id,Date,Task_title, Task_Detail,Status):
    conn=sqlite3.connect("To_Do.db")
    cur=conn.cursor()
    cur.execute("UPDATE Task_manager1 SET Date=?,Task_title=?,Task_Detail=?, Status=? WHERE id=?",(Date,Task_title, Task_Detail,Status,id))
    conn.commit()
    conn.close()

##print(view())
##print("\n\n")
##print(view_for_excel_generation())
