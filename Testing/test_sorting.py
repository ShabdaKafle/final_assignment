import unittest
import Frontend.records

class Test_Record(unittest.TestCase):
    def setUp(self):
        self.sort = Frontend.records.Record

    def test_sort_records(self):
        list = [("shabda", "kafle", "123", "abc"), ("john", "cena", "234", "def"), ("fara", "den", "567", "red"), ("rose", "willaim", "678", "yxz")]
        expectedresult = [["john", "cena", "234", "def"],["fara", "den", "567", "red"],["shabda", "kafle", "123", "abc"],["rose", "willaim", "678", "yxz"]]
        sctaulresult = self.sort.sort_records(self.sort.sort_records,list)
        self.assertEqual(expectedresult, sctaulresult)


