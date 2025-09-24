class Customer:
    #راح اضمنه بعدين في سي اس في
    def __init__(self, account_id=None,first_name=None,last_name=None , password=None ,checking_balance = 0.0, savings_balance= 0.0, id=None,name=None):
        # نستقبل قيم العميل و اضفت رصيد
        #ننادي التست
        
        self.id=id if id is not None else str(account_id)if account_id is not None else None
        self.name=mame if name is not None else str(account_id)if account_id is not None else None

        

        self.account_id= account_id
        self.first_name= first_name 
        self.last_name= last_name 
        self.password= password 
        self.checking_balance= float(checking_balance)
        self.savings_balance= float(savings_balance)
        # القيم بدون الطلبات