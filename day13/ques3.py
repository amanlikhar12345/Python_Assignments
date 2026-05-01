'''3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''
num=int(input("enter the number"))
x=0
if num<=1:
    print("Composite Number")
else:
    for i in range(2,num//2):
        if num%i==0:
            x=1
            break
if x==1:
    print("Composite Number")
else:
    print("not Composite Number")