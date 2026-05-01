'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''
import math
num=int(input("enter the number "))
n=num+1

while True:
    x=1
    if n<1:
        print("not prime number")
    
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                x=0
                break
        if x==1:
            print("Next Prime = ",n)
            gap=n-num
            print("Gap = ",gap)
            break
    n+=1
