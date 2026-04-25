"""Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""
sec=int(input("Total seconds = "))
hour=sec//3600
sec=sec%3600
min=sec//60
s=sec%60
print(f"Hours = {hour}\nMinutes = {min}\nSeconds = {s}")