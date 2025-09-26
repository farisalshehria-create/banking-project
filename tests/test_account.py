import unittest
from bank.account import Account 
# نستورد الملفات للكلاس
class TestAccount ( unittest.TestCase):

    def test_deposit(self):
        acc = Account(500.0)# رصيدي
        acc . deposit(200.0)# ايداعل

        self.assertEqual(acc.balance, 700.0)

    def test_withdraw(self):

        acc = Account(2000.0)
        acc . withdraw(500.0)
        self.assertEqual(acc.balance, 1500)
    def test_withdraw_overdraft(self):#اذا سحبت اكثر من رصيدي
        acc = Account(1000.0)
        #اذا سحب اكثر يطلع ارور
        with self.assertRaises(ValueError):

            acc.withdraw(1500.0)

if __name__ == "__main__":
    unittest.main()
