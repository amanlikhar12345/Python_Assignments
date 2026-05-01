'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
import math
num=int(input("enter the number"))
n=num+1
n1=num-1
x=1
if num<1:
   x=0
else:
    for i in range(2,(num//2)+1):
        if num%i==0:
            x=0
            break
if x==1:
    print("prime number")
    while True:
        if n<1:
            print("not prime number")
        else:
            for j in range(2,int(math.sqrt(n)+1)):  
                
                if n%j==0:
                    break
            else:
               print("Next Prime = ",n)
               break
        n+=1
else:
    print("not prime number")
    while True:
        if n1<1:
            print("not prime number")
        else:
            for a in range(2,int(math.sqrt(n1)-1)+1):  
                
                if n1%a==0:
                    break
            else:
               print("previous Prime = ",n1)
               break
        n1-=1



