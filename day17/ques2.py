'''2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
'''

num=input("Input:")
first=0
second=0

for i in range(0,len(num)//2):
    first=first+int(num[i])
print("First Half Sum = ",first)

for i in range(len(num)//2,len(num)):
    second=second+int(num[i])
print("Second Half Sum = ",second)

if first==second:
    print("Balanced Number")
else:
    print("Unbalanced Number")
