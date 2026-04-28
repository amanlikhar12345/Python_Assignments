'''9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''
num=int(input("enter the number"))
step=""
rem=num%10
num=num//10
while num>0:
    rem1=num%10
    num=num//10
    diff=rem1-rem
    if diff<0:
        diff=-(diff)
    diff=str(diff)
    step=step+ diff
    rem=rem1
l=len(step)
step=int(step)
print("step differnces = ",step)
sum=0
lar=0
while step>0:
    rem=step%10
    step//=10
    if rem>lar:
        lar=rem
    sum+=rem
print("largest = ",lar)
print("sum = ",sum)
if sum%l==0:
    print("Balanced Number")
else:
    print("unnBalanced Number")