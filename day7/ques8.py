'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
'''
tem=int(input("Enter temperature: "))
if tem<=0:
    print("Weather Condition: Freezing")
elif tem>0 and tem<20:
    print("Weather Condition: Cold")
elif tem>=21 and tem<35:
    print("Weather Condition: Warm")
else:
    print("Weather Condition: Hot")