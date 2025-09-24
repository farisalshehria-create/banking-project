class Account:
    def __init__(self,balance=0.0):
        #عشان تسوي حساب جديد
        self.balance = float(balance)
        #احفظ فلوسه 
        #كيف يودع؟
                            #صحح mony ب money
        def deposit(self, mony):
            self.balance +=mony
        def withdraw(self,mony):
            #تاكد من المبلغ المسحوب
            if mony <= self.balance:
                #بعد التاكيد ان المبلغ كافي وحول يخصم المبلغ
                self.balance -= mony 
                return True
            else:
                return False
                
