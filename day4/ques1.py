'''---

Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---
'''
bill=int(input("enter the bill amount :"))
gst=int(input("enter the GST :"))
ser=int(input("enter the service charges :"))
friend=int(input("enter the number of friend :"))
final=(bill*gst)/100+(bill*ser)/100+bill
each=final/friend
print(f"Final Bill = {final}\nEach Person Pays = {each}")