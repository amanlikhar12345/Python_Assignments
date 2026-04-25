'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome
'''
n=int(input("n = "))
rev=0
n1=n
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
if rev==n1:
    print("Palindrome")
else:
    print("not Palindrome")