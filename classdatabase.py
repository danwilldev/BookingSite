import sqlite3
conn = sqlite3.connect('data/classdatabase.db', check_same_thread=False)
c = conn.cursor()

class ClassDatabase():
    def __init__(self, day, name, time, location):
        self.location = location
        self.time = time
        self.day = day
        self.name = name

    def create(self):
        try:
            c.execute('''CREATE TABLE classes
            (day text, name text, time text, location text)''')
            conn.commit()
        except:
            print("DB already created")
        else:
            print("Fatal Error")

    def add(self):
        c.execute('INSERT INTO classes(day, name, time, location) VALUES(?,?,?,?)',
                  (self.day, self.name, self.time, self.location))
        conn.commit()


    @staticmethod
    def classdetails():
        try:
            c.execute('SELECT * FROM classes')
            item = c.fetchall()
            return item
        except:
            return False
    """@staticmethod
    def classdetails(day):
        try:
            c.execute('SELECT * FROM classes WHERE day=?',(day,))
            item = c.fetchone()
            details = [item[0], item[1], item[2], item[3]]
            return details
        except:
            return False"""
        

    
