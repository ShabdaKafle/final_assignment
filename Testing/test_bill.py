import unittest
import model.bill

class Test_Bill(unittest.TestCase):

    def setUp(self):
        self.b = model.bill.Bill()

    def test_set_bill_number(self):
        self.b.set_bill_num(89)
        self.assertEqual(89, self.b.get_bill_num())  # Test Passed
        self.b.set_bill_num(1234)
        self.assertNotEqual(123, self.b.get_bill_num())  # Test Passed

    def test_set_name(self):
        self.b.set_name("abc")
        self.assertEqual("abc", self.b.get_name())  # Test Passed
        self.b.set_name("wxyz")
        self.assertNotEqual("xyz", self.b.get_name())  # Test Passed

    def tearDown(self):
        del self.b



