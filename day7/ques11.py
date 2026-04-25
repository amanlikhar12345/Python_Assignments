'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''
dis=int(input("Enter distance: "))
clas=input("Enter class (Sleeper or AC): ").lower()
if dis<=100:
    if clas=="ac":
        fare=200
    else:
        fare=100
elif dis>101 and dis<500:
    if clas=="ac":
        fare=600
    else:
        fare=300
else:
    if clas=="ac":
        fare=1000
    else:
        fare=500
print("Total Fare: ₹",fare)

