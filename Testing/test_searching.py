import unittest
import Frontend.search_students

class Test_Search(unittest.TestCase):
    def setUp(self):
        self.lst = [('shabda', 'Bcd'), ("sarina", "Def"), ('srishti', 'Abc')]
        self.s = Frontend.search_students.Search(self)

    def Test_serch(self):
        index = 0

        item = "Shabda"

        expected_result = "Shabda"

        result = self.so.serch(index, item)

        actual_result = result[0][0]  # index 0 = First Name

        self.assertEqual(expected_result, actual_result)  # Test Passed


