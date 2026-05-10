'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''
num=int(input("enter the number"))
l=len(str(num))
num=int(num)
sum=0
smal=num

print("Products: ",end=" ")
for i in range(1,l):
    rem=num%10
    num//=10
    rem1=num%10
    prod=rem*rem1 
    sum+=prod
    print(prod,end=" ")
    if prod<smal:
        smal=prod

print()
print("Smallest = ",smal)

print("Sum = ",sum)
if sum%l==0:
    print("Stable Number")
else:
    print("Unstable Number")