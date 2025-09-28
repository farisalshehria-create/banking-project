import unittest
from bank.account import Account 
# نستورد الملفات للكلاس
class TestAccount ( unittest.TestCase):
# الايداع <><><><><><><><><><><><>><><><><><>
    def test_deposit(self):
        acc = Account(500.0)# رصيدي
        acc . deposit(200.0)# ايداعل

        self.assertEqual(acc.balance, 700.0)
#السحب <><><><><<<><><><><<<<><><><<><>
   # اذا سحب اقل من الرصيد
    def test_withdraw(self): 

        acc = Account(2000.0)
        acc . withdraw(500.0)
        self.assertEqual(acc.balance, 1500)
    #اذا سحبت الي بالرصيد كامل
    def test_withdraw_all_balance(self):
        acc = Account(1000.0)
        acc .withdraw(1000.0)
        self.assertEqual(acc.balance, 0.0)
        #اذا سحبت وتطبقت الرسوم
    def test_withdraw_overdraft_withinLimit(self):
        acc = Account(500.0)
        acc.withdraw(550.0)
        self.assertEqual(acc.balance, -85.0)

    #اذا سحبت عالحافة
    def test_withdraw_overdraft_min100(self):
        acc = Account(2000.0)
        acc.withdraw(2065)
        self.assertEqual(acc.balance, -100.0)


    #اذا سحبت اكثر من رصيد
    def test_withdraw_overdraft(self):
        acc = Account(1000.0)
        with self.assertRaises(ValueError): #اذا سحب اكثر يطلع ارور
            
            acc.withdraw(1500.0)

if __name__ == "__main__":
    unittest.main()
