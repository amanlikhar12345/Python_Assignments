'''
**12. Multiplication of Digits**
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to **find the product of all digits of a number using loops and then check whether the result is even or odd**.

Input: 1234
Output: 24
Even
'''
prod=1
num=int(input("enter the number"))
while num>0:
    rem=num%10
    num=num//10
    prod*=rem
print(prod)
if prod%2==0:
    print("Even")
else:
    print("Odd")    