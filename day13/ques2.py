'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
import math
num=int(input("enter the number "))
n=num+1

while True:
    x=1
    if n<1:
        print("not prime number")
    
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                x=0
                break
        if x==1:
            print("Next Prime = ",n)
            break
    n+=1
