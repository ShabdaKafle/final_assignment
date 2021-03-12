import unittest
import Frontend.records

class Test_Record(unittest.TestCase):
    def setUp(self):
        self.lst = [('shabda', 'Bcd'), ("sarina", "Def"), ('srishti', 'Abc')]
        self.s = Frontend.records.Record(self)




    def test_sort_records(self):

        expected_result = [("sarina", "Def"), ('shabda', 'Bcd'), ('srishti', 'Abc')]

        actual_result = self.s.sort_records(self.lst, 0)

        self.assertEqual(expected_result, actual_result)

        expected_result = [('srishti', 'Abc'), ('shabda', 'Bcd'), ("sarina", "Def")]

        actual_result = self.s.sort_records(self.lst, 1)

        self.assertEqual(expected_result, actual_result)