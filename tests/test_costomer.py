import unittest 
from bank.customer import Customer #اخذ كلاس الكوستمر ونجربه

from bank.account import Account #تجربة كاينات اكاون

class TestCust(unittest.TestCase): #
    def test_cust_id(self): # id pass name
        cust = Customer(id="10001" , name="Faris" , password="Aa123456")# 

        self.assertEqual(cust.id , "10001")


        self.assertEqual(cust.name , "Faris")
        self.assertEqual(cust.password , "asd123456")


    def test_acco_id(self):

        cust = Customer(id="10002", name="Rose", password="asd654321")

        self.assertEqual(cust.checking, Account)
        self.assertEqual(cust.checking.balance, 0.0)

        self.assertEqual(cust.savings.balance, 0.0)
    
    # تجربة الاختبار 
if __name__ == "__main__":

    unittest.main()