'''7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime
'''
num=int(input("Input:"))
i=1
sum=0
while num>0:
    rem=num%10    
    num=num//10

    if i%2==1:
        sum+=rem
    i+=1
print("Alternate Sum = ",sum)
if sum<1:
    print("not prime number")
else:
    for x in range(2,sum):
        if sum%x==0:
             print("not prime number")
             break
    else:
        print("prime number")