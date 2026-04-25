"""Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z
"""
event_duration=int(input("enter the total time of event in second"))
hour=event_duration//3600

left=event_duration%3600

minute=left//60

#second=event_duration-(hour*60*60+minute*60)
sec=left%60
print(F"Hours: {hour}, Minutes: {minute}, Seconds: {sec}")

