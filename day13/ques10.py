'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''
num=int(input("enter the number "))
zero=0
sum=0
s=9
while num>0:
    rem=num%10
    num=num//10
    if rem==0:
        zero+=1
    sum+=rem
    if rem<s:
        s=rem
print("Zero Count = ",zero)
print("Sum = ",sum)
print("Smallest Digit = ",s)
t=sum*s
print("Final Result = ",t)
if t<1:
    print("not prime number")
else:
    for i in range(2,t//2):
        if t%i==0:
            x=1
            break
    if x==0:
        print("Prime Number")
    else:
        print("not prime number")
