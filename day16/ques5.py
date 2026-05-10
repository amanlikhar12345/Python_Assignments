'''5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern'''
num=input("enter the number")
res=0
for i in range(0,len(num)):
    r=int(num[i])
    if i%2==0:
        res+=r
    else:
        res-=r
print("Result = ",res)
if res>=0:
    print("Positive Pattern")
else:
    print("Negative Pattern")