'''---

Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2

---
'''
a,b,c,d,e=map(int,input("enter the mark of all 5 subject :").split())
total=a+b+c+d+e
avg=total/5
per=(total/500)*100
print(f"Total = {total}\nAverage = {avg}\nPercentage = {per}")