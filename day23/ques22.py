'''
A
AB
A C
A  D
ABCDE
'''

n=int(input("enter the number"))
ch=66
for i in range(1,n+1):
    print()
    print("A",end="")
    for j in range(2,i+1):
        
        if i==j:
            print(chr(ch),end="")
            ch+=1

        else:
            print(" ",end="")

    if i==n:
            
        print(chr(ch),end="")
        ch+=1