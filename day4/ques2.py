'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

'''
mob=int(input("enter the amount of mobile price :"))
down=int(input("enter the amount of down payment :"))
intrest=int(input("enter the value of interest :"))
month=int(input("enter the month you want EMI :"))
remain=mob-down
total_amt=int((remain*intrest)/100+remain)
emi=total_amt/month
print(f"Remaining Amount = {remain}\nTotal with Interest = {total_amt}\nMonthly EMI = {emi}")

