'''4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''

num=input("Input:")
max=0
count=0

print("Max Difference = ",end=" ")
for i in range(0,len(num)-1):
    n1=int(num[i])
    n2=int(num[i+1])
    diff=abs(n1-n2)
    print(diff,end=" ")
    if max<diff:
        max=diff
    if diff>2:
        count+=1

print()
print("Count (>2) = ",count)
print("Max Difference = ",max)
if max>=2:
   print("Smooth Number")
else:
   print("Irregular Pattern")
