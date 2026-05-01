'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
num=int(input("enter the number "))
even=0
odd=0
while num>0:
    rem=num%10
    num=num//10
    if rem%2==0:
        even+=1
    else:
        odd+=1
if even>=odd:
    diff=even-odd
else:
    diff=odd-even

x=0
if diff<=1:
    print("not prime number")
else:
    for i in range(2,diff//2):
        if diff%i==0:
            x=1
            break
    if x==0:
        print("Prime Number")
    else:
        print("not prime number")
print("Even Count = ",even)
print("Odd Count = ",odd)
print("Difference = ",diff)

