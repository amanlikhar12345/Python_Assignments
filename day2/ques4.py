"""========================================
Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300
"""
dis=int(input("enter the traveled kilometers"))
fare=15*dis
print(f"Distance = {dis} \nTotal Fare = {fare}")