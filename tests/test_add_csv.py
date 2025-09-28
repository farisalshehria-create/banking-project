import unittest
import os #lip
#from bank.customer import Customer
from bank.main import add_cost, rows_csv
BANK_CSV = "bank.csv"
class TestaddCSV (unittest.TestCase):
    def test_add_customer_row(self):
        
        countBefore = len(rows_csv())# عشان يشغله ويقرا كل الصفوف
        add_cost("10010", "Nora", "M", "cxz123456", 500.0,2000.0)#نظيف عميل جديد
       
        countAfter = len(rows_csv())# يحسب الصفوف
        self.assertEqual(countAfter, countBefore + 1)# kjh;] lk lkil dsh,,k 1

        last_row = rows_csv() [-1]# التعريفر عشان الاختبار

        self.assertEqual(last_row[0], "10010")
        self.assertEqual(last_row[1], "Nora")
        self.assertEqual(last_row[2], "M")
        self.assertEqual(last_row[3], "cxz123456")
        self.assertEqual( float (last_row[4]), 500.0)
        self.assertEqual( float (last_row[5]), 2000.0)
        

if __name__ == "__main__":
    unittest.main()





