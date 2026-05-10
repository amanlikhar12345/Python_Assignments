'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
'''
num=input("Input:")
max=0
even=0
p1=int(num[0])
p2=int(num[1])
p=abs(p1-p2)


print("Differences: ",end=" ")
for i in range(0,len(num)-1):
    n1=int(num[i])
    n2=int(num[i+1])
    diff=abs(n1-n2)
    print(diff,end=" ")
    if diff%2==0:
        even+=1
    if diff>max:
        max=diff

print()

print("Even Differences Count = ",even)
print("Max Difference = ",max)
if diff==p:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")




























'''while num>10:
    rem=num%10
    num=num//10
    rem1=num%10
    print(num)
    diff=abs(rem-rem1)
    print(diff,end=" ")
    if diff%2==0:
        even+=1
    if diff>max:
        max=diff

print()
print("Even Differences Count = ",even)
print("Max Difference = ",max)'''
    