'''14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7'''

n=int(input("enter the number"))
ch=1
for i in range(1,n+1):
    print()
    for j in range(1,n+1):
       print(ch,end=" ")
       ch+=1