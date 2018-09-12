import sqlite3
from passlib.hash import sha256_crypt
conn = sqlite3.connect('database.db')
c = conn.cursor()
 #hash
passwordhash = sha256_crypt.hash("djhewufhu23r82urjfnjkdshfkjh8ry8yuwhe23rj")
print(hash)
 def create():
    try:
        #Creating the table for logins
        c.execute('''CREATE TABLE users
        (username text, password text)''')
        conn.commit()
        c.execute('''CREATE TABLE usersinfo
        (address text, phone integer)''')
    except:
        print("DB already created")
    else:
        print("Fatal Error")
 def hash(username, password):
    password_hash =  sha256_crypt.encrypt(password)
    add(username, password_hash)
        
def add(username, password):
    c.execute('INSERT INTO users(username, password) VALUES(?,?)', (username, password))
    print('User inserted {} {}'.format(username, password))
    conn.commit()
def check():
    #passableusername = "'{}'".format(username)
    #print(passableusername)
    c.execute('SELECT * FROM users WHERE username=?',(username,))
    user = c.fetchone()
    if sha256_crypt.verify(password, user[1]) == True:
    #if user[1] == password:
        print("You have entered the correct password")
        print("Welcome {}".format(user[0]))
    else:
        print("Password incorrect")
        
 """if str(input("Would you like to create an account y/n ")) == "y":
    create()
    #username = str(input("Enter Username : "))
    #password = str(input("Enter Password : "))
    hash(str(input("Enter Username : ")), str(input("Enter Password : ")))
 else:
    if str(input("Would you like to Sign In y/n ")) == "y":
        username = str(input("Enter Username : "))
        password = str(input("Enter Password : "))
        check()
    else:
        pass
""" 
