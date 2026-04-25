'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''
amt=int(input("Enter bill amount: "))
if amt<1000:
    final=(amt*5)//100
elif amt>1001 and amt<5000:
    final=(amt*12)//100
    if amt>3000:
        final+=200
else:
    final=((amt*18)//100)+200
bill=final+amt
print("Final Bill Amount: ₹",bill)

