'''2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''
num=int(input("Input :"))
num1=num
sum=0
prod=1
while num>0:
    rem=num%10
    num=num//10
    sum+=rem
    prod*=rem
diff=abs(sum-prod)
diff=str(diff)
l=len(diff)
diff=int(diff)
final=l+diff

print("Sum = ",sum)
print("Product = ",prod)
print("Difference = ",diff)
print("Digits = ",l)
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

