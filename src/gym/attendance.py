from datetime import date, datetime
#global function for transforming date
def convert_date(day):
    return datetime.strptime(day, '%y/%m/%d').date()


#create function for attendance table
def create(con, attendance):
    query = f"INSERT into Attendances ({','.join(attendance.keys())}) values ({','.join('?'*len(attendance))})"
    cur = con.cursor()
    cur.execute(query, tuple(attendance.values()))
    con.commit()
    rowid = cur.lastrowid
    cur.execute("SELECT * from Attendances where user=? and day=?", (attendance['user'],str(date.today())))
    return cur.fetchone()


#list function for attendance table
def list_(con):
    cur = con.cursor()
    cur.execute("SELECT * from Attendances")
    results =  cur.fetchall()
    if results:
        return results 

def detail(con, username, day):
    cur = con.cursor()
    query = "SELECT * from Attendances where user=? and day=?"
    cur.execute(query, (username,day))
    result = cur.fetchone()
    if result:
        return result
    else:
        print("The attendance or user doesnot exist")
        

#update function for attendance 
def update(con, username, day, present):
    cur = con.cursor()
    query = f"UPDATE Attendances set present=? Where user=? and day=?"
    cur.execute(query, (present,username,day))
    con.commit()
    cur.execute("SELECT * from Attendances where user=? and day=?", (username,day))
    return cur.fetchone()



def delete(con,username, day):
    cur = con.cursor()
    try:
        cur.execute("DELETE from Attendances where user=? and day=?", (username,day))
        con.commit()
        return True
    except Exception as e:
        print(str(e))

def list_in_date(con,day):
    cur = con.cursor()
    cur.execute("Select * from Attendances WHERE day=?", (day,))
    return cur.fetchall()
