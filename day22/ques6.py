'''6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9'''


n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for j in range(n-i,0,-1):
        print("-",end="")
    for k in range(1,i+1):
        print(k+(i-1),end="")