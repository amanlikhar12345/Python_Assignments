'''16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321
'''

n=int(input("enter the number"))

for i in range(1,n+1):
    print()
    for j in range(n-i,0,-1):
        print(" ",end="")

    for k in range(1,i+1):
        print(k,end="")
  
    for l in range(i-1,0,-1):
        print(l,end="")