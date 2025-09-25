import csv #مكتبة سسف
BANK_CSV= "bank.csv" # مسار الملف في روت

def rows_csv(): # عشان اخلي كل سطر بالقائمة
    
    with open(BANK_CSV,"r",newline="")as f: #

        reader = csv.reader(f)
        return list(reader)
def add_cost(account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0):
    with open(BANK_CSV,"a",newline="")as f: #

        writer = csv.writer(f)
        writer.writerow([account_id, first_name, last_name, password, balance_checking, balance_savings])
# عشان نحفظ بيانات العميل
