'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''

t=int(input("enter the total mark :"))
o=int(input("enter the obtained mark :"))
per=(o/t)*100
print("Percentage = ",per)
