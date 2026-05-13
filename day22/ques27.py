'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''
n=int(input("enter the number"))
ch=1

for i in range(1,n+1):
    print()
    for j in range(n-i,0,-1):
        print(" ",end="")

    for k in range(1,i+1):
        print(ch,end=" ")
        ch+=1
