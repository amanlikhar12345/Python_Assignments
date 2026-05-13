'''
A
BB
CCC
DDDD
EEEEE




'''
ch=65
n=int(input("enter number"))
for i in range(1,n+1):
    print()

    for j in range(1,i+1):
         print(chr(ch),end="")
    ch+=1