import unittest
import model.user

class Test_Bill(unittest.TestCase):

    def setUp(self):
        self.u = model.user.User()

    def test_set_username(self):
        self.u.set_username("nina")
        self.assertEqual("nina", self.u.get_username())  # Test Passed
        self.u.set_username("abcd")
        self.assertNotEqual("nina", self.u.get_username())  # Test Passed

    def test_set_contact(self):
        self.u.set_contact(98765)
        self.assertEqual(98765, self.u.get_contact())  # Test Passed
        self.u.set_contact(879)
        self.assertNotEqual(98, self.u.get_contact())  # Test Passed

    def tearDown(self):
        del self.u