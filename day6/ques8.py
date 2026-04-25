"""8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120 else:
   
                print("Highest Stock = ",e)
        else:
            print("Highest Stock = ",d)   
    else:
        print("Highest Stock = ",c)  
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500"""
a=int(input("Unit1 = "))
b=int(input("Unit2 = "))
c=int(input("Unit3 = "))
d=int(input("Unit4 = "))
e=int(input("Unit5 = "))
f=int(input("Unit6 = "))
if a>b:
    if a>c:
        if a>d:
            if a>e:
                if a>f:
                    print("Highest Stock = ",a)
                else:
                    print("Highest Stock = ",f)
            else:
                if e>f:
                    print("Highest Stock = ",e)   
                else: 
                    print("Highest Stock = ",f)    
        else:
            if d>e and d>f:
                print("Highest Stock = ",d)   
            else: 
                if e>d:
                      print("Highest Stock = ",e)
                else:
                    print("Highest Stock = ",f)
    else:
        if c>d and c>e and c>f:
            print("Highest Stock = ",c)   
        else:
            if d>e and d>f:
                print("Highest Stock = ",d)  
                if e>f:
                    print("Highest Stock = ",e)  
                else:
                    print("Highest Stock = ",f)
else:
    if b>c:
        if b>d:
            if b>e:
                if b>f:
                    print("Highest Stock = ",b)
                else:
                    print("Highest Stock = ",f)
            else:
                if e>f:
                    print("Highest Stock = ",e)   
                else: 
                    print("Highest Stock = ",f)    
        else:
            if d>e and d>f:
                print("Highest Stock = ",d)   
            else: 
                if e>d:
                      print("Highest Stock = ",e)
                else:
                    print("Highest Stock = ",f)
    else:
        if c>d and c>e and c>f:
            print("Highest Stock = ",c)   
        else:
            if d>e and d>f:
                print("Highest Stock = ",d)  
                if e>f:
                    print("Highest Stock = ",e)  
                else:
                    print("Highest Stock = ",f)
 
                 