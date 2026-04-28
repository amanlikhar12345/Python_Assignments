'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number

'''
n=int(input("enter the num"))
sum=0
n1=n
fact=1
while n>0:
    rem=n%10
    n=n//10
    fact=1
    for i in range(1,rem+1):
        fact=i*fact
    sum=fact+sum
    print(sum)
if n1==sum:
    print("strong number")
else:
    print("not strong number")