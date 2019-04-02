import sqlite3
from passlib.hash import sha256_crypt
import uuid
conn = sqlite3.connect(
    'data/database.db', check_same_thread=False)
c = conn.cursor()
passwordhash = sha256_crypt.hash(
    "djhewufhu23r82urjfnjkdshfkjh8ry8yuwhe23rj")  # hash


class Database():
    def __init__(self, email, firstname, lastname, phone, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.password = password

    def create(self):
        try:
            c.execute('''CREATE TABLE users
            (userid text, email text, password text)''')
            conn.commit()
            c.execute('''CREATE TABLE usersinfo
            (userid text, firstname text, lastname text, phone text)''')  # phone not integer as python doesnt support
            conn.commit()
        except:
            print("DB already created")
        else:
            print("Fatal Error")

    def hashpw(self):
        self.password_hash = sha256_crypt.encrypt(self.password)

    def add(self):
        # Making a random uuid using the python uuid moduel, 4 is the only truly random.
        userid = str(uuid.uuid4())
        c.execute('SELECT * FROM users WHERE userid=?', (userid,))
        conn.commit()

        c.execute('INSERT INTO users(userid, email, password) VALUES(?,?,?)',
                  (userid, self.email, self.password_hash))
        c.execute('INSERT INTO usersinfo(userid, firstname, lastname, phone) VALUES(?,?,?,?)',
                  (userid, self.firstname, self.lastname, self.phone))
        print('User inserted {} {} {}'.format(
            userid, self.email, self.password_hash))
        conn.commit()

    @staticmethod
    def check(email, password):
        try:
            c.execute('SELECT * FROM users WHERE email=?',(email,))
            item = c.fetchone()
            if sha256_crypt.verify(password, item[2]) == True:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def uuid(email):
        try:
            c.execute('SELECT * FROM users WHERE email=?',(email,))
            item = c.fetchone()
            return str(item[0])
        except:
            return False

    @staticmethod
    def userdetails(uuid):
        try:
            c.execute('SELECT * FROM usersinfo WHERE userid=?',(uuid,))
            item = c.fetchone()
            details = [item[1], item[2], item[3]]
            return details
        except:
            return False
