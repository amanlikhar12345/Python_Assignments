'''2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N'''

import math
n1=int(input("enter the start range :"))
n2=int(input("enter the end range :"))
for i in range(n1,n2+1):
    sq=i*i
    cu=i**3
    root=math.sqrt(i)
    print("Numner is :",i)
    print("Square is :",sq)
    print("Cube is :",cu)
    print("Square Root is :",root)