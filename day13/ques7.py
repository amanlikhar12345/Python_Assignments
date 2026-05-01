'''7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
num=int(input("enter the number"))
sum=0
while num>0:
    rem=num%10
    num=num//10
    sum=sum+rem
print("Sum = ",sum)
x=0
if sum<1:
    print("not prime number")
else:
    for i in range(2,sum//2):
        if sum%i==0:
            x=1
            break
if x==0:
    print("lucky Number")
else:
    print("Normal number")