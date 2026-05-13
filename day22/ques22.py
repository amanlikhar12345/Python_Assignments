'''22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''

n=int(input("Enter the number"))
for r in range(1,n*2):
    print("*",end='')

for i in range(n,0,-1):
    print()
    for j in range(n-i,0,-1):
        print(" ",end="")

    for k in range(1,i+1):
        if k==1 :
            print("*",end="")
        else:
            print(" ",end="")
        

    for x in range(n+1,i+n):
        if x!=i+(n-1):
            print(" ",end="")
        else:
            print("*",end="")
print()

