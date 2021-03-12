import unittest
import Backend.dbconnection

class Test_DBConnect(unittest.TestCase):
    def setUp(self):
        self.db = Backend.dbconnection.DBConnect()

    def test_select(self):
        query ="select * from student_data "
        row = self.db.select(query)
        self.assertIsNotNone(row)

    def test_insert(self):
        query = "insert into bill_data(bill_number, date, student_name, room_type, month_of_paying, total_fees, \
        user_id) values(%s,%s,%s,%s,%s,%s,%s)"
        bill = str(input('enter the bill number: '))
        date = str(input('enter the date: '))
        name = str(input("Enter the student name: "))
        room = str(input('enter the room type: '))
        month = str(input('enter the month: '))
        fee = str(input('enter the fees: '))
        id = str(input("enter the user id: "))
        values = (bill,date,name,room, month, fee, id)
        self.db.insert(query, values)
        query = "select * from student_data"
        row = self.db.select(query)
        self.assertIsNotNone(row)

