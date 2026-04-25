'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
'''
sal=int(input("enter the monthly salary "))
day=int(input("enter the working days "))
hours=int(input("enter the hours of working per day "))
sal_day=sal/day
sal_hour=sal_day/8
print(f"Salary per day = {sal_day}\nSalary per hour = {sal_hour}")