'''3)	WAP to find out all the leap years between two entered years'''

n1=int(input("enter the start range :"))
n2=int(input("enter the end range :"))
for  i in range(n1,n2+1):
    if (i%4==0 and i%100!=0) or i%400==0:
         print(i)


