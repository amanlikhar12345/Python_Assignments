'''----------------------------------------
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------'''
wage,days=map(int,input("enter the daily wage and number of days").split(","))
sal=wage*days
print(f"Daily Wage = {wage}")
print(f"Days = {days}")
print(f"Salary = {sal}")