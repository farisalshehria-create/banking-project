from .account import Account
class Customer:
    #راح اضمنه بعدين في سي اس في
    def __init__(self,id,name, password,checking_balance = 0.0, savings_balance= 0.0):

        # نستقبل قيم العميل و اضفت رصيد
        #ننادي التست
        
        
        #
        
        self.checking = Account(checking_balance)
        self.savings= Account (savings_balance)
        #
        

        self.id= str(id)
        self.name=name 
        #self.last_name= last_name 
        self.password= password 
        self.checking_balance= Account(checking_balance)
        self.savings_balance= Account(savings_balance)
        # القيم بدون الطلبات