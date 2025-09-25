import unittest 
from bank.customer import Customer #اخذ كلاس الكوستمر ونجربه

from bank.account import Account #تجربة كاينات اكاون

class TestCust(unittest.TestCase): #
    def test_cust_id(self): # id pass name
        cust = Customer(id="10001" , first_name="Faris" ,last_name="ALshehri", password="asd123456")# 

        self.assertEqual(cust.id , "10001")


        self.assertEqual(cust.first_name , "Faris")
        self.assertEqual(cust.last_name , "ALshehri")
        self.assertEqual(cust.password , "asd123456")


    def test_acco_id(self):

        cust = Customer(id="10002", first_name="Rose",last_name="saeed", password="asd654321")

        self.assertEqual(type(cust.checking), Account)
        self.assertEqual(cust.checking.balance, 0.0)

        self.assertEqual(cust.savings.balance, 0.0)
    
    # تجربة الاختبار 
if __name__ == "__main__":

    unittest.main()