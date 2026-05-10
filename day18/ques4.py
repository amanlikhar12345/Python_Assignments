'''4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
'''
unit=int(input("enter the unit"))
bill=unit*5 if unit<100 else 7*(unit-100)+500 if unit<200 else 10*(unit-300)+1900
print(bill)