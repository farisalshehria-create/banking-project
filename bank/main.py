
import csv
from bank.customer import Customer
from bank.account import Account

# ملف سسف في جذر المشروع
BANK_CSV = "bank.csv"

# تقرأ كل الصفوف من سسق
def rows_csv():
    with open(BANK_CSV, "r", newline="") as f:
        return list(csv.reader(f))

# كتب كل الصفوف للملف
def write_all_rows(rows):
    with open(BANK_CSV, "w", newline="") as f:

        writer = csv.writer(f)
        writer.writerows(rows)

# إضافة عميل جديد
def add_cost(account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0):
    with open(BANK_CSV, "a", newline="") as f:

        
        writer = csv.writer(f)
        
        writer.writerow([account_id, first_name, last_name, password, balance_checking, balance_savings])


#العمليات
def load_customer(account_id, password=None):
    for r in rows_csv():
        # شكل الصف:
        if len(r) < 6:
            continue

        if r[0] == str(account_id):

            if password is not None and r[3] != password:
                raise ValueError("incorrect password")
            
            return Customer(
                id=r[0],
                first_name=r[1],
                last_name=r[2],
                password=r[3],
                checking_balance=float(r[4]),
                savings_balance=float(r[5]),



            )
    raise ValueError("account not found")

# نحدّث أرصدة العميل داخل سسف بعد أي عملية
def save_customer_balances(customer: Customer):
    rows = rows_csv()

    for i, r in enumerate(rows):
        if len(r) >= 6 and r[0] == str(customer.id):

            rows[i][4] = str(customer.checking.balance)
            rows[i][5] = str(customer.savings.balance)
            write_all_rows(rows)
            
            return
    raise ValueError("account not found when saving")

# المنيو
def main():
    print("welcome to Faris Bank")
    while True:

        print("\n-- menu --")
        print("1 add new customer")
        print("2 deposit")

        print("3 withdraw")
        print("4 transfer (same customer)")
        print("5 exit")
        choice = input("choose number:").strip()

        try:
            if choice == "1":

                # إضافة عميل جديد صفر
                account_id = input("Account ID: ").strip()

                first_name = input("First name: ").strip()

                last_name = input("Last name: ").strip()
                password = input("Password: ").strip()
                #gh.l hgvwd] wtv
                add_cost(account_id, first_name, last_name, password, 0.0, 0.0)
                print("customer added")

            elif choice == "2":
                # إيداع
                acc_id = input("Account ID: ").strip()
                pwd = input("Password: ").strip()
                
                acct = input("Deposit to (checking/savings): ").strip().lower()
                amount = float(input("Amount: ").strip())


                c = load_customer(acc_id, pwd)
                if acct == "checking":

                    c.checking.deposit(amount)

                elif acct == "savings":
                    c.savings.deposit(amount)
                else:
                    print("Invalid account type")
                    continue
                save_customer_balances(c)
                print("deposit done")

            elif choice == "3":
                # سحب
                acc_id = input("Account ID: ").strip()
                pwd = input("Password: ").strip()
                acct = input("Withdraw from (checking/savings): ").strip().lower()
                amount = float(input("Amount: ").strip())

                c = load_customer(acc_id, pwd)
                if acct == "checking":
                    c.checking.withdraw(amount)
                elif acct == "savings":
                    c.savings.withdraw(amount)
                else:
                    print("Invalid account type")
                    continue
                save_customer_balances(c)
                print("Withdraw done ")

            elif choice == "4":
                # تحويل بين حساب نفس العميل


                acc_id = input("Account ID: ").strip()
                pwd = input("Password: ").strip()

                from_acct = input("From (checking/savings): ").strip().lower()
                to_acct = input("To (checking/savings): ").strip().lower()

                amount = float(input("Amount: ").strip())

                c = load_customer(acc_id, pwd)
#
                c.transfer(from_acct, to_acct, amount)
                save_customer_balances(c)

                print("ransfer done")
#اطلع
            elif choice == "5":
                print("bye")
                break

            else:
                print("Invalid choice, try again.")

#
        except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
