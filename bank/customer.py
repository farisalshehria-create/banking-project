from .account import Account
class Customer:
    #راح اضمنه بعدين في سي اس في
    def __init__(self,id,first_name,last_name, password,checking_balance = 0.0, savings_balance= 0.0):

        # نستقبل قيم العميل و اضفت رصيد
        #ننادي التست
        
        
        #
        
        self.checking = Account(checking_balance)
        self.savings= Account (savings_balance)
        #
        

        self.id= str(id)
        self.first_name=first_name 
        self.last_name=last_name 
        self.password= password 
        #حساب العميل 
        self.checking_balance= Account(checking_balance)
        self.savings_balance= Account(savings_balance)
        # القيم بدون الطلبات

#العمليات
    def transfer(self, from_acct, to_acct, money):

        if money <=0:
            raise ValueError("worong ! invalid number")
    
        if from_acct == "checking" and to_acct == "savings":

            if self.checking.balance < money:
                raise ValueError("balance does not allow")
            self.checking.withdraw(money)
            self.savings.deposit(money)

            return True
        elif from_acct == "savings" and to_acct == "checking":
            if self.savings.balance < money:

                raise ValueError("balance does not allow")
            self.savings.withdraw(money)
            self.checking.deposit(money)

            return True 
        else:
            raise ValueError("invalid accounts")
    
