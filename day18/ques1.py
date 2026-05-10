'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
'''
type=input("enter the customer type(regular or premium)")
amt=int(input("enter the shoping amount"))
dis=(amt*20)//100 if type=="premium" and amt>5000  else (amt*10)//100 if amt<5000 else (amt*10)//100  if type=="regular" and amt>3000 else (amt*5)//100
print("discount = ",dis) 
bill=amt-dis
print("Final bill = ",bill)