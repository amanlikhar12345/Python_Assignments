'''------------------------------------------------------------
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
----------------------------------------------------------------
'''
amt=int(input("enter the bill of shoping :"))
dis=(amt*10)/100
final=amt-dis
print(f"Discount = {dis}")
print(f"Final = {final}")