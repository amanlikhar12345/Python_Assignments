'''4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''
num=input("enter the number")

n1=int(num[0])
n2=int(num[1])
initial=abs(n2-n1)
for i in range(2,len(num)-1):
    p1=int(num[i])
    p2=int(num[i+1])
    pat=abs(p2-p1)
    if initial!=pat:
        print("Pattern Break Detected")
        break
else:
    print("Consistent Pattern")
print("Initial Gap = ",initial)