'''
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *'''

n=int(input("enter the number"))
for i in range(1,n+1):
    print()
    if i%2!=0:
        print("* "*n)
    else :
        print(" *"*(n-1))