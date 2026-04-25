'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''
p=int(input("enter the principal amount :"))
r=int(input("enter the rate of interest :"))
t=int(input("enter the duration :"))
c=p*(1+r/100)**t-p
d=p+c
print("Amount = ",d)
print("Compound Interest = ",c)