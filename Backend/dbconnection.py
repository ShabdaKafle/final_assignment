import mysql.connector

class DBConnect:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', password = '9865191484', database='billing_system')
        self.cur = self.con.cursor()

    def insert(self, query, values):
        self.cur.execute(query,values)
        self.con.commit()

    def select(self,query, values=None):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows