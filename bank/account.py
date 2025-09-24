class Account:
    def __init__(self,balance: float=0.0):
        #عشان تسوي حساب جديد
        self.balance = float(balance)
        #احفظ فلوسه 
        #كيف يودع؟A
                            #صحح mony ب money
        #الايداع لازم فوق 0 
    def deposit(self, money: float):
        if money <= 0:
            raise ValueError("worong ! invalid number")
            
        self.balance += float(money)
        return self.balance
            
            
    def withdraw(self,money: float):
            #تاكد من المبلغ المسحوب
            #لذل الرصيد لايسمح
        if money <= 0:
            raise ValueError("you balance is not enough")
            #ممنوع يودع اكضر من رصيده
        if money > self.balance:
            raise ValueError("balance does not allow")
                #بعد التاكيد ان المبلغ كافي وحول يخصم المبلغ
            self.balance -= float (money) 
            return self.balance
