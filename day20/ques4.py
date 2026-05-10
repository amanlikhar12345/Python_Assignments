'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
n1=int(input("Enter starting number: "))
n2=int(input("Enter ending number: "))



print("Armstrong Numbers are:")
for i in range(n1,n2+1):
    temp=i
    arm=0		
    while temp>0:
        rem=temp%10
        arm=arm+rem**len(str(i))
        temp=temp//10
    if i==arm:
        print(arm)
       