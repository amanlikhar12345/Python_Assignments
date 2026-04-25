'''------------------------------------------
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
----------------------------------------------'''
l,b=map(int,input("enter the length or breadth").split())
a=l*b
print(f"Area = {a}")