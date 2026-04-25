'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
'''
speed=int(input("enter the speed "))
a,b=map(int,input("enter the time in hours_minute").split("_"))
time=a+(b/60)
dist=speed*time
print(f"Total Time = {time} hours\nDistance = {dist} km")