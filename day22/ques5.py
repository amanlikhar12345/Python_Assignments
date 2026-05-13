'''5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''
n=int(input("enter the number"))

for i in range(n,1,-1):
    print()
    for j in range(1,i):
        print(j,end="")
    for x in range(i+1,(n+1)):
        print("*"*2,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
        