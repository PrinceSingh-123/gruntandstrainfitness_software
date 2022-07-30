
#create function for revenue table
def create(con, revenue):
    query = f"INSERT into Revenues ({','.join(revenue.keys())}) values ({','.join('?'*len(revenue))})"
    cur = con.cursor()
    cur.execute(query, tuple(revenue.values()))
    con.commit()
    rowid = cur.lastrowid
    cur.execute("SELECT * from Revenues where id=?", (rowid,))
    return cur.fetchone()

#list function for revenue table
def list_(con):
    cur = con.cursor()
    cur.execute("SELECT * from Revenues")
    results =  cur.fetchall()
    if results:
        return results

def detail(con, id):
    cur = con.cursor()
    cur.execute("SELECT * from Revenues where id=?", (id,))
    result = cur.fetchone()
    if result:
        return result
    else:
        print("The revenue doesnot exist") 

#update function for revenue 
def update(con, id, revenue):
    cur = con.cursor()
    query = f"UPDATE Revenues set {'=?,'.join(revenue.keys())+'=?'} Where id=?"
    data = list(revenue.values())
    data.append(id)
    cur.execute(query, tuple(data))
    con.commit()
    cur.execute("SELECT * from Revenues where id=?", (id,))
    return cur.fetchone()

def delete(con,id):
    cur = con.cursor()
    try:
        cur.execute("DELETE from Revenues where id=?", (id,))
        con.commit()
        return True
    except Exception as e:
        print(str(e))

def total(con):
    cur = con.cursor()
    cur.execute("Select sum(amount) from Revenues")
    return cur.fetchone()[0]

def total_in_days(con, days):
    cur = con.cursor()
    cur.execute(f"Select sum(amount) from Revenues WHERE added_at > DATETIME('now', '-{days} day')")
    return cur.fetchone()[0]
