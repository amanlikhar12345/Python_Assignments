'''11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1'''
n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for j in range(1,i):
        print(j,end="")
    for k in range(i,(n)+1):
        if i==1:
             print()
        else:
             print(" "*2,end="")
        
    for l in range(i-1,0,-1):
        print(l,end="")

for x in range(n+1,1,-1):
    
    print()
    for y in range(1,x):
        print(y,end="")
    for z in range(n+1,x,-1):
        if x==1:
             print()
        else:
             print(" "*2,end="")
        
    for m in range(x-1,0,-1):
        print(m,end="")
