
#create function for staff table
def create(con, staff):
    query = f"INSERT into Staffs ({','.join(staff.keys())}) values ({','.join('?'*len(staff))})"
    cur = con.cursor()
    cur.execute(query, tuple(staff.values()))
    con.commit()

    #returning last record 
    rowid = cur.lastrowid
    cur.execute("SELECT * from Staffs where id=?", (rowid,))
    return cur.fetchone()


#list function for staff table
def list_(con):
    cur = con.cursor()
    cur.execute("SELECT * from Staffs")
    results =  cur.fetchall()
    if results:
        return results

def detail(con, id):
    cur = con.cursor()
    cur.execute("SELECT * from Staffs where id=?", (id,))
    result = cur.fetchone()
    if result:
        return result
    else:
        print("The staff doesnot exist")
        
#update function for staff 
def update(con, id, staff):
    cur = con.cursor()
    query = f"UPDATE Staffs set {'=?,'.join(staff.keys())+'=?'} Where id=?"
    data = list(staff.values())
    data.append(id)
    cur.execute(query, tuple(data))
    con.commit()
    cur.execute("SELECT * from Staffs where id=?", (id,))
    return cur.fetchone()

def delete(con,id):
    cur = con.cursor()
    try:
        cur.execute("DELETE from Staffs where id=?", (id,))
        con.commit()
        return True
    except Exception as e:
        print(str(e))

def req_pay(con,id):
    cur= con.cursor()
    cur.execute("SELECT id,name,due_amount FROM Staffs where id=?",(id,))
    return cur.fetchone()

def generate_due(con,id, amount, day):
    cur = con.cursor()
    query = "UPDATE Staffs SET due_amount=?,generate_date=? where id=?"
    cur.execute(query,(amount,day,id))
    con.commit()
    cur.execute("SELECT * from Staffs where id=?", (id,))
    return cur.fetchone()

