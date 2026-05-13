'''8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5
'''

n=int(input("enter the number"))
for i in range(n):
    print()

    if i==0 :
        for j in range(5):
            print(j+1,end=" ")
       
    elif i == n-1:
        for j in range(5):
            print("5",end=" ")

    else :
        for v in range(5):
            if v==0:
                print(i+1,end=" ")
            elif v==4:
            
                print(n,end=" ")

            else:
                print(" ",end=" ")