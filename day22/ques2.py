'''2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********'''

n=int(input("enter the number"))
for i in range(n):
    print()

    if i==0 or i==n-1:
        for j in range(9):
            print("*",end="")
       


    else :
        for v in range(9):
            if v==0 or v == 8:
                print("*",end="")
            else:
                print(" ",end="")