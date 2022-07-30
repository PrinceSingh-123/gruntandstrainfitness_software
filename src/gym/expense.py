
#create function for expense table
def create(con, expense):
    query = f"INSERT into Expenses ({','.join(expense.keys())}) values ({','.join('?'*len(expense))})" 
    cur = con.cursor()
    cur.execute(query, tuple(expense.values()))
    con.commit()
    rowid = cur.lastrowid
    cur.execute("SELECT * from Expenses where id=?", (rowid,))
    return cur.fetchone()

#list function for expense table
def list_(con):
    cur = con.cursor()
    cur.execute("SELECT * from Expenses")
    results =  cur.fetchall()
    if results:
        return results

def detail(con, id):
    cur = con.cursor()
    cur.execute("SELECT * from Expenses where id=?", (id,))
    result = cur.fetchone()
    if result:
        return result
    else:
        print("The expense doesnot exist")
        
#update function for expense 
def update(con, id, expense):
    cur = con.cursor()
    query = f"UPDATE Expenses set {'=?,'.join(expense.keys())+'=?'} Where id=?"
    data = list(expense.values())
    data.append(id)
    cur.execute(query, tuple(data))
    con.commit()
    cur.execute("SELECT * from Expenses where id=?", (id,))
    return cur.fetchone()

def delete(con,id):
    cur = con.cursor()
    try:
        cur.execute("DELETE from Expenses where id=?", (id,))
        con.commit()
        return True
    except Exception as e:
        print(str(e))

def total(con):
    cur = con.cursor()
    cur.execute("Select sum(amount) from Expenses")
    return cur.fetchone()[0]

def total_in_days(con, days):
    cur = con.cursor()
    cur.execute(f"Select sum(amount) from Expenses WHERE added_at > DATETIME('now', '-{days} day')")
    return cur.fetchone()[0]