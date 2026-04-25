'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''
num=int(input("enter the number"))
p=int(input("enter the power"))
sum=1
while p>0:
    sum*=num
    p-=1
print("output = ",sum)