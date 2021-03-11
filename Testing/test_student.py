import unittest
import model.student
class Test_Grades(unittest.TestCase):
    def setUp(self):
        self.s = model.student.Student()

    def test_set_name(self):
        self.s.set_name("name")
        self.assertEqual("name",self.s.get_name())  # Test Passed
        self.s.set_name("abcd")
        self.assertNotEqual("abc", self.s.get_name())  # Test Passed


    def test_set_parents_number(self):
        self.s.set_parents_number(98102)
        self.assertEqual(98102,self.s.get_parents_number())  # Test Passed
        self.s.set_parents_number(1090)
        self.assertNotEqual(1000, self.s.get_parents_number())  # Test Passed

    def test_set_room_type(self):
        self.s.set_room_type("3-seater")
        self.assertEqual("3-seater",self.s.get_room_type())  # Test Passed
        self.s.set_room_type("2-seater")
        self.assertNotEqual("seater", self.s.get_room_type())  # Test Passed

    def tearDown(self):
        del self.s


