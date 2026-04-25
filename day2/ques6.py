"""========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
"""
amt=int(input("enter  the amount"))
ten=amt//10
left=amt%10
five=left//5
print(f"Amount = ₹{amt}")
print(f"Output = ₹10 * {ten}")
print(f"Output = ₹5 * {five}")
