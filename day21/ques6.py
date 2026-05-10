'''6)
a
ab
abc
abcd
abcde
'''
n=int(input("enter the number"))
i=1
while i<=n:
    print()
    j=1
    ch=97
    while j<=i:
         print(chr(ch),end="")
         j+=1
         ch+=1
    i+=1