'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''
num=int(input("enter the number "))
s=9
l=0
while num>0:
    rem=num%10
    num=num//10
    if rem>l:
        l=rem
    if rem<s:
        s=rem
t=s+l
x=0
if t<=1:
    print("not prime number")
else:
    for i in range(2,t//2):
        if t%i==0:
            x=1
            break
print("Smallest = ",s)
print("Largest = ",l)
print("Sum = ",t)
if x==0:
    print("Prime Number")
else:
    print("not prime number")