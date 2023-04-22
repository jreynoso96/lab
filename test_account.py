import unittest
from account import *


class Test(unittest.TestCase):
    def setUp(self):
        self.a1 = Account('John')
        self.a2 = Account('Daisy')

    def tearDown(self):
        del self.a1
        del self.a2

    def test_init(self):
        self.assertEqual(self.a1.get_name(),'John')
        self.assertEqual(self.a2.get_name(),'Daisy')
        self.assertEqual(self.a1.get_balance(),0)
        self.assertEqual(self.a2.get_balance(),0)

        self.assertTrue(self.a1.deposit(50))
        self.assertFalse(self.a2.deposit(-50))

        self.assertEqual(self.a1.get_balance(),50)
        self.assertEqual(self.a2.get_balance(), 0)

        self.assertTrue(self.a1.withdraw(25))
        self.assertFalse(self.a2.withdraw(50))
        self.assertFalse(self.a2.withdraw(-50))

        self.assertEqual(self.a1.get_balance(), 25)
        self.assertEqual(self.a2.get_balance(), 0)

if __name__ == "__main__":
    unittest.main()
