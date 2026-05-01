'''4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''
num=int(input("Input:"))

while num>0:
    rem=num%10
    num=num//10
    rem=str(rem)
    num=str(num)
    if rem in num:
        print("reject")
        break
    num=int(num)
else:
    print("Valid Unique Code")