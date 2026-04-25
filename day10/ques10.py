'''**10. Even Numbers Between Two Numbers**
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to **display all even numbers between two numbers using loops**.

Input: 10, 20
Output: 10 12 14 16 18 20
'''
num1=int(input("enter the 1 even num "))
num2=int(input("enter the 2 even num "))
for i in range(num1,num2+1,2):
    print(i,end=" ")