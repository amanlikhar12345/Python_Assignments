'''
9.
    1
   10
  101
 1010
10101

'''
n=int(input("enter the rows"))
i=1
while i<=n:
    sp=1
    while sp<=(n-i):
        print(" ",end="")
        sp+=1
    j=1
    while j<=i:
        if j%2!=0:
            print("1",end="")
        else:
            print("0",end="")
        j+=1
    i+=1    
    print()




