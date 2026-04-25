'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
'''
d=int(input("enter the distance in km "))
m=int(input("enter the milage "))
p_price=int(input("enter the price of petrol "))
p_used=d/m
p_cost=p_used*p_price
print(f"Petrol Used = {p_used}\nTotal Cost = {p_cost}")


