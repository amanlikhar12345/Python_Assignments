'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()

    for k in range(i,1,-1):
        print(k+(i-2),end="")

    for j in range(n-i,0,-1):
        print("-",end="")