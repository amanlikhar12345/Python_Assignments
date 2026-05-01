'''9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''
num=int(input("Input:"))
sum=1
for i in range(2,(num//2)+1):
    if num%i==0:
        sum+=i
if sum>num:
    print("Abundant Number")
else:
    print("Not Abundant Number")