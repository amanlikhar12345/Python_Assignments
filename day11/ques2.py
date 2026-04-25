'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2
'''
num=int(input("enter the number"))
small=9
while  num>0:
    rem=num%10
    num=num//10
    if rem<small:
        small=rem
print("Smallest Digit = ",small)