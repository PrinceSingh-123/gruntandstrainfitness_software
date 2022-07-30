from posixpath import split
from PIL import Image
import io
from gym.utils import check_email

class InvalidEmail(Exception):
    pass

class RequiredError(Exception):
    pass

#global function to convert file into binary
def convert_into_binary(file_path):
    basewidth = 400
    baseheight = 500
    img = Image.open(file_path)
    format = img.format
    if img.size[0] < img.size[1]:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    else:
        hpercent = (baseheight/float(img.size[1]))
        wsize = int((float(img.size[0])*float(hpercent)))
        img = img.resize((wsize,baseheight), Image.ANTIALIAS)
    output = io.BytesIO()
    img.save(output, format=format)
    return output.getvalue()

#create function for user table
def create(con, user):
    if user['username'] and user['email'] and user['name'] and user['membership_type']:
        if check_email(user['email']):
            if user.get('profile_pic'):
                user['profile_pic'] = convert_into_binary(user['profile_pic'])
            query = f"INSERT into Users ({','.join(user.keys())}) values ({','.join('?'*len(user))})"
            cur = con.cursor()
            cur.execute(query, tuple(user.values()))
            con.commit()
            query = "SELECT username,email,name,membership_type,age,address,profile_pic,bio from Users where username=?"
            cur.execute(query,(user['username'],))
            return cur.fetchone()
        else:
            raise InvalidEmail("Entered email is not valid")
    else:
        raise RequiredError("All required input should be given")

#list function for user table
def list_username(con):
    cur = con.cursor()
    cur.execute("SELECT username from Users")
    results =  cur.fetchall()
    if results:
        return results

def single_detail(con, username):
    cur = con.cursor()
    query = "SELECT username,email,name,membership_type,age,address,profile_pic,bio from Users where username=?"
    cur.execute(query, (username,))
    result = cur.fetchone()
    if result:
        return result
    else:
        print("something wrong")

def list_detail(con):
    cur = con.cursor()
    query = "SELECT username,email,name,membership_type,age,address,profile_pic,bio from Users"
    cur.execute(query)
    results = cur.fetchall()
    if results:
        return results  

#update function for user 
def update(con, username, user):
    cur = con.cursor()
    if user['email'] and user['name'] and user['membership_type']:
        if check_email(user['email']):
            if user.get('profile_pic'):
                user['profile_pic'] = convert_into_binary(user['profile_pic'])
            query = f"UPDATE Users set {'=?,'.join(user.keys())+'=?'} Where username=?"
            data = list(user.values())
            data.append(username)
            cur.execute(query, tuple(data))
            con.commit()
            cur.execute("SELECT username,email,name,membership_type,age,address,profile_pic,bio from Users where username=?",(username,))
            return cur.fetchone()
        else:
            raise InvalidEmail("Entered email is not valid")
    else:
        raise RequiredError("All required input should be given")

def delete(con,username):
    cur = con.cursor()
    try:
        cur.execute("DELETE from Users where username=?", (username,))
        con.commit()
        return True
    except Exception as e:
        print(str(e))
