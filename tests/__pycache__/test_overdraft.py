import unittest
from bank.account import Account
#شرط رسوم 35 و ممنوع الرصيد يقل عن 100
class TestOverdraft(unittest.TestCase):
    def test_min100(self):
        acc =Account(100.0)
        acc .withdraw(165.0) # 100-156= -65

        self.assertEqual(acc.balance, -100.0)# -65 -35=-100
if __name__ == "___main_":
    unittest.main()