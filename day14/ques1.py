'''1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''
num=int(input("Input:"))
num1=num
rem=0
sum=0
rev=0
while num>0:
    rem=num%10
    num=num//10
    sum+=rem
    rev=rev*10+rem
diff=abs(num1-rev)
final=diff+sum
print("Sum of Digits = ",sum)
print("Reverse = ",rev)
print("Difference = ",diff)
print("Final Result = ",final)


if final<1:
   print("not prime number")
else:
    for i in range(2,final):
        if final%i==0:
            print("not prime number")
            break
    else:
        print("prime nubmer")