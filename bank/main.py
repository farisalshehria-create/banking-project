import csv #مكتبة سسف
BANK_CSV= "bank.csv" # مسار الملف في روت

def rows_csv(): # عشان اخلي كل سطر بالقائمة
    
    with open(BANK_CSV,"r",newline="")as f: #

        reader = csv.reader(f)
        return list(reader)
