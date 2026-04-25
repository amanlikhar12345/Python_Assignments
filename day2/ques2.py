"""Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz
"""
age=int(input("enter the your age"))
days_lived=365*age
hours_lived=24*days_lived
minute_lived=60*hours_lived
seconds_lived=60*minute_lived
print("You've lived approximately: ")
print("Days: ",days_lived)
print("Hours: ",hours_lived)
print("Minute: ",minute_lived)
print("Seconds: ",seconds_lived)
