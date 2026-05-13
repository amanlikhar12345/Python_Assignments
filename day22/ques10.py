'''10) Slanted Star Block
    ****
     ****
      ****
       ****
'''
n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")