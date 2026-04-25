'''----------------------------------------------------------------------
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''
km=int(input("enter the distance in KM :"))
mil=int(input("enter the milage oof the vehical per litre :"))
pp=int(input("enter the prize of petrol :"))
cost=(km/mil)*pp
print(f"cost = {cost}")