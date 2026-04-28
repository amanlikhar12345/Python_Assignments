'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''
num1=int(input("enter the first number"))
num2=int(input("enter the second  number"))
count=0
for i in range(num1,num2+1):
    if i%7==0:
        count+=1
print("count = ",count)