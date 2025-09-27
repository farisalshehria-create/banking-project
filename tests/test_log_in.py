import unittest
from bank.customer import Customer

class testpass(unittest.TestCase):
    def testPassRight(self): # اذا الباس صحيح:
        c= Customer(id="10100", first_name="bodoor", last_name="SH", password="vbnm123456")
        self.assertTrue(c.check_password ("vbnm123456")
                        )
        
       #
       #
       #  اذا غلط
    def testPassWrong(self):
        c= Customer(id="10200", first_name="mozoon", last_name="ri", password="vbnm654321")

        with self.assertRaises(ValueError):
        
            c.check_password("woromg")
if __name__ == "__main__":
    unittest.main()