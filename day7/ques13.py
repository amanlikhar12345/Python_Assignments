'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''
sal=int(input("Enter salary: "))
rate=int(input("Enter rating (1–5): "))
if rate==5:
    incr=(sal*25)//100
elif rate==4:
    incr=(sal*20)//100
elif rate==3:
    incr=(sal*10)//100
elif rate==2:
    incr=(sal*5)//100
else:
    incr=0
if sal<20000 and rate>=4:
    incr+=2000
final=sal+incr
print("Revised Salary: ₹",final)