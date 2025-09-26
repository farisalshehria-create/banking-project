import unittest
from bank.account import Account 
# نستورد الملفات للكلاس
class TestAccount ( unittest.TestCase):

    def test_deposit(self):
        acc = Account(500.0)# رصيدي
        acc . deposit(200.0)# التحويل

        self.assertEqual(acc.balance, 300.0)

    def test_withdraw(self):

        acc = Account(2000.0)
        acc . withdraw(500.0)
        self.assertEqual(acc.balance, 1500)
    def test_withdraw_overdraft(self):#اذا سحبت اكثر من رصيدي
