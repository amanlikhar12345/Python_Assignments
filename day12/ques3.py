'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
'''
num1=int(input("enter the first number"))
num2=int(input("enter the second  number"))
for i in range(num1,num2+1):
    if i%10==5:
         print(i,end=" ")
 