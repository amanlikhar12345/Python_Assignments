'''6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''
num=int(input("enter the number "))
x=0
if num<=3:
    print("not Composite Number")
else:
    for i in range(4,num//2):
        if num%i==0:
             x=1
             break
if x==1:
    print("Composite Number")
else:
    print("not Composite Number")

count=0
j=1
while num>=j:
    if num%j==0:
        count+=1
    j+=1
print("Factors Count = ",count)

fact=0
for x in range(2,num//2):
    if num%x==0:
        fact=x
        break
print("Smallest Factor = ",fact)
    