https://github.com/users/farisalshehria-create/projects/1/views/1

BANK PROJECT
Small startup bank project using Python , To practice OOP programming style
File handling (CSV), and test follow-up (TDD)
It contains:
_Add new customers to the system (saved in bank.csv).
_Each customer can have checking and/or savings accounts.
_Deposit money into checking or savings.
_Withdraw money (with overdraft protection rules).
_Transfer money between accounts (checking<>savings).
_Password validation for login.
_Exception handling (e.g., wrong password, overdraft > 100 USD).

How to Run ?

python -m unittest discover -s tests -p "test_*.py" -v

ok! in RPEL?

py

#                                we will take classes
>>> from bank.account import Account
>>> from bank.customer import Customer
#                               you can try simple cases
#                         create a quick account containing 100$
>>> rar = Account(100.0)
#                                 deposit an amount     
>>> rar.deposit(50)
#                                   print balance
>>> print(rar.balance)
#                                 withdraw an ammount
>>> rar.withdraw(30)
#                   with draw an ammount exceeding the overdrawn balance
>>> mar = Account(1000)
>>> acc3.withdraw(1101)
ValueError: you cant your balance > -100

# These were quick tests
# but there are tests from scratch!
#                                    create account
>>> Ali = Customer(id="60010", first_name="Ali", last_name="saeed", password="qwer1234", checking_balance=0.
0,savings_balance=0.0)
#                             if you enter the worong password
>>> Ali.check_password("hjhgklb")
ValueError: in correct password
#                                   but if it is true
>>> Ali.check_password("moon1234")
True
#                                  Transfer to account
>>> Ali.checking.deposit(3000)
3000.0
#                          Transfer from a checking to a saving
>>> Ali.transfer("checking", "savings",50)
True
# you can do the opposite!
#                               print checking and saving
>>> print(Ali.checking.balance, Ali.savings.balance)
2950.0 50.0
#                                       CSV  
>>> from bank.main import add_cost, rows_csv
#                      read and memorize the number of rows in before
>>> before = len(rows_csv())
#                                   add new row
>>> add_cost("80010", "try", "useer", "rows1234", 10.0, 20.0)
#                      read and memorize the number of rows in after
>>> after = len(rows_csv())
#                              print before and after
>>> print(before, after)
18 19
#                               read and last row
>>> print(rows_csv()[-1])
['80010', 'try', 'useer', 'rows1234', '10.0', '20.0']
#                                   Exit REPL
>>> exit()