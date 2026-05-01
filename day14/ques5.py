'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''
num=int(input("Input:"))
while num>0:
    rem=num%10    
    num=num//10
    rem1=num%10   
    if rem1>rem:
       print("Unstable Number")
       break
else:
    print("Stable Number")
