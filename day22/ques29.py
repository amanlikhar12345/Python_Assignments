'''29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()

    for k in range(1,i):
        print("-",end=" ")

    for j in range(1,2):
        print(i,end=" ")
  
    for l in range(n-i,0,-1):
        print("-",end=" ")
