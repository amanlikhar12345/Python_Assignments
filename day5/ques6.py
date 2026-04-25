'''6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert
'''
tem=int(input("Enter temperature: "))
humi=int(input("Enter humidity: "))
if tem>=32:
    print("Hot day")
if humi>=75:
    print("High humidity alert")