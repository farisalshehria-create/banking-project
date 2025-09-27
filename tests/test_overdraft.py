import unittest
from bank.account import Account
#شرط رسوم 35 و ممنوع الرصيد يقل عن 100
class TestOverdraft(unittest.TestCase):
    def test_min100(self):
        acc =Account(100.0)
        acc .withdraw(165.0) # 100-156= -65

        self.assertEqual(acc.balance, -100.0)# -65 -35=-100

        
    #رفض السحب اذا الرصيد -100
    def test_reject_min100(self):
        acc =Account(100.0)
        with self.assertRaises(ValueError):
            acc .withdraw(166.0) #100 - 166 = -66 - 35 = -101
            
            
if __name__ == "___main_":
    unittest.main()

