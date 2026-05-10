'''8.
enter n6
 654321
  65432
   6543
    654
     65
'''

n=int(input("enter the number"))

for i in range(1,n):
    print()
    for j in range(1,i):
        print(" ",end="")
    for k in range(n,i-1,-1):
        print(k,end="")