'''6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''
import math
num=int(input("enter the number"))
n=num+1
while True:
    x=1
    if n<1:
        x=0
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                x=0
                break
        if x==1:
            print("Next Prime Cabin = ",n)
            break
        
    n+=1
