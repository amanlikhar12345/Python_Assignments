'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''
cost=int(input("enter the cost price  "))
sell=int(input("enter the selling price  "))
profit=sell-cost
per=(profit/cost)*100
print("Profit % = ",per)
print("Profit = ",profit)


