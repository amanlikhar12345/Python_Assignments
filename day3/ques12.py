'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''
amt=int(input("enter the total amount :"))
h=amt//100
l=amt%100
f=l//50
l=l%50
t=l//10
print("₹100 x ",h)
print("₹50 x ",f)
print("₹10 x ",t)
