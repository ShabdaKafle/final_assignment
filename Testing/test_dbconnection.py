import unittest
import Backend.dbconnection

class Test_DBConnect(unittest.TestCase):
    def setUp(self):
        self.db = Backend.dbconnection.DBConnect

    def test_select(self):
        query3 = 5
        self.assertRaises(TypeError, self.db.select, query3)
        query = "select * from student_data"
        row = self.db.select(query)
        self.assertIsNotNone(row)

    def test_insert(self):
        query = "insert into student_table(name) values=%s"
        values = ("shabda")
        self.db.insert(query, values)
        query = "select * from student_data"
        row = self.db.select(query)
        self.assertIsNotNone(row)
