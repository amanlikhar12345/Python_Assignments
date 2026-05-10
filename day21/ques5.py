'''5)
A
AB
ABC
ABCD
ABCDE
'''

n=int(input("enter the number"))


i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=i:
         print(chr(ch),end="")
         j+=1
         ch+=1
    i+=1