'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''
h=int(input("enter the hours :"))
m=int(input("enter the minutes :"))
s=int(input("enter the seconds :"))
t=s+m*60+h*3600
print(f"Total Seconds = {t}")