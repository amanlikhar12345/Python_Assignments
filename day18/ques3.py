'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
'''
exp=int(input("enter the experience"))
sal=int(input("enter the salary"))
bonus=(30*sal)//100 if exp>10  else (20*sal)//100 if exp>10  else (10*sal)//100 
final=sal+bonus
print("salary after bonus is "final)