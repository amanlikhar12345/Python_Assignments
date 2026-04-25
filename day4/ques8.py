'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

'''
p=int(input("enter the principal amount"))
r=int(input("enter the rate of interest"))
t=int(input("enter the time in year"))
ci=p*(1+(r/100))**t-p
amt=ci+p
print(f"Amount after interest = {amt}")