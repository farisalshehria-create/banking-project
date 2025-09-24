class Account:
    def __init__(self,balance=0.0):
        #عشان تسوي حساب جديد
        self.balance = float(balance)
        #احفظ فلوسه 
        #كيف يودع؟
                            #صحح mony ب money
        def deposit(self, mony):
            self.balance +=mony
            return self.balance
            if mony <=0:
                raise ValueError("worong ! invalid number")
            
        def withdraw(self,mony):
            #تاكد من المبلغ المسحوب
            #لذل الرصيد لايسمح
            if mony <= self.balance:
                raise ValueError("you balance is not enough")
                #بعد التاكيد ان المبلغ كافي وحول يخصم المبلغ
                self.balance -= mony 
                return True
            else:
                return False
                
