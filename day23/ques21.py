'''
1
22
3 3
4  4
55555



'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    print(i,end="")
    for j in range(2,i+1):
        
        if i==j:
            print(j,end="")
        elif i==n:
            print(,end="")
        else:
            print(" ",end="")