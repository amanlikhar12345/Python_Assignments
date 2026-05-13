'''13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5'''   
n=int(input("Enter the number"))

for i in range(n,1,-1):
    print()
    for j in range(n-i,0,-1):
        print(" ",end="")

    for k in range(1,i+1):
        if k==1 :
            print(k+(n-i),end="")
        else:
            print(" ",end="")
        

    for x in range(n+1,i+n):
        if x!=i+(n-1):
            print(" ",end="")
        else:
            print(x-(n),end="")

for i in range(1,n+1):
    print()
    for j in range(n-i,0,-1):
        print(" ",end="")

    for k in range(1,i+1):
        if k==1 :
            print(i,end="")
        else:
            print(" ",end="")
        

    for x in range(n+1,i+n):
        if x!=i+(n-1):
            print(" ",end="")
        else:
            print(i,end="")
