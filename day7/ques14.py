'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''
program=5000
design=4000
marketing=3000

course=input("Enter course category: ").lower()
type=input("Enter user type: ").lower()
if course=="programming":
    if type=="student":
        amt=(program*20)//100
    elif type=="Working Professional":
        amt=I(program*10)//100
    else:
        amt=0
    final=program-amt

elif course=="design":
    if type=="student":
        amt=(design*20)//100
    elif type=="Working Professional":
        amt=I(design*10)//100
    else:
        amt=0
    final=design-amt
else:
    if type=="student":
        amt=(marketing*20)//100
    elif type=="Working Professional":
        amt=I(marketing*10)//100
    else:
        amt=0
    final=marketing-amt
print("Final Course Fee: ₹",final)
