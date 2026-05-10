'''3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found
'''
num=input("Input:")
count=0
x=0

print("Matching Digits: ",end=" ")
for i in range(1,len(num)-1):
    sum=int(num[i-1])+int(num[i+1])
    if int(num[i])==sum:
        print(int(num[i]),end=" ")
        count+=1
        x+=1
print()
print("Count = ",count)
if x>0:
    print("Neighbor Sum Pattern Found")
else:
    print("No Matching Digit")