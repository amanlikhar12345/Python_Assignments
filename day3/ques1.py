'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
'''
dis=int(input("enter the distance in kilometer"))
time=int(input("enter the time in hours"))
speed=dis/time
print(f"Distance = {dis}")
print(f"Time = {time}")
print(f"Speed = {speed}")