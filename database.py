import sqlite3
from passlib.hash import sha256_crypt
conn = sqlite3.connect('data/database.db')
c = conn.cursor()
passwordhash = sha256_crypt.hash("djhewufhu23r82urjfnjkdshfkjh8ry8yuwhe23rj") #hash

class Database():
    def __init__(self, email , firstname, lastname, phone, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.password = password
    def create(self):
        
        try:
            c.execute('''CREATE TABLE users
            (email text, password text)''')
            conn.commit()
            c.execute('''CREATE TABLE usersinfo
            (firstname text, lastname text, phone text)''')#phone not integer as python doesnt support
            conn.commit()
        except:
            print("DB already created")
        else:
            print("Fatal Error")
    def hashpw(self):
        self.password_hash =  sha256_crypt.encrypt(self.password)
    def add(self):
        
        c.execute('INSERT INTO users(email, password) VALUES(?,?)', (self.email, self.password_hash))
        c.execute('INSERT INTO usersinfo(firstname, lastname, phone) VALUES(?,?,?)', (self.firstname, self.lastname, self.phone))
        print('User inserted {} {}'.format(self.email, self.password_hash))
        conn.commit()
    def check(self, email, password):
        c.execute('SELECT * FROM users WHERE email=?',(email,))
        user = c.fetchone()
        if sha256_crypt.verify(password, user[1]) == True:
            return True
        else:
            return False
    
        
"""db = Database("danwill1210@gmail.com", "Dan", "Will", "07956775948" , "Goon1234pw")
db.create()
db.hashpw()
db.add()
db.check("danwill1210@gmail.com", "Goon1234pw") TEST INPUTS"""
