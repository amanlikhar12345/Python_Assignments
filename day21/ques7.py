'''7.
enter n6
     *
    **
   ***
  ****
 *****
******
'''

n=int(input("enter the number"))
x=1

for i in range(n+1,1,-1):
    print()

    for j in range(1,i):
         print(" ",end="")

    for k in range (0,x):
         print("*",end="")
    x+=1
