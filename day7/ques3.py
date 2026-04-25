'''3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
'''
annual=int(input("Enter annual income: "))
if annual<=250000:
    print("No tax")
elif annual>250000 and annual<=500000:
    annual-=250000
    tax=(annual*5)//100
elif annual>500000 and annual<=1000000:
    annual-=250000
    tax=(annual*20)//100
else:
    annual-=250000
    tax=(annual*30)//100
print("Tax Payable: ",tax)