'''
25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print(j,end="")
    for j in range(n-i,0,-1):
        print(j,end="")


for i in range(n-1,0,-1):
    print()
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print(j,end="")
    for j in range(n-i,0,-1):
        print(j,end="")