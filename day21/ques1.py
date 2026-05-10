'''1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''

sum=0
n1=int(input("enter the start range :"))
n2=int(input("enter the end range :"))
for i in range(n1,n2+1):
    if i%9==0:
        sum+=i
   
print(sum)