'''5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number         
'''

num=input("Input:")
first=""
second=""
x=0

for i in range(0,len(num)):
    n=int(num[i])
    if n%2==0:
       x=1
    
if x==1:
    for i in range(0,len(num)//2):
        first=first+num[i]
    print("First Half = ",first)
   
    for i in range(len(num)//2,len(num)):
        second=second+num[i]
    print("Second Half = ",second)

f=int(first)
s=int(second)
sum=f+s
sq=sum**2

print("Sum = ",sum)
print("Square = ",sq)
d=int(num)
if sq==d:
    print("Tech Number ")
else:
    print("Non Tech Number  ")
