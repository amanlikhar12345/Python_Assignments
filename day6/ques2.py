'''2. An e-commerce website provides discounts based on the cart value and user type. 
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000, 
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise, 
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
'''
value=int(input("Cart Value = "))
user=input("User Type (premium or regular) = ")
if value>=5000:
    if user=="premium":
        dis=(value*20)//100
        
    else:
        dis=(value*10)//100
elif value<5000 and value>=2000:
    dis=(value*5)//100
else:
    dis=0
amt=value-dis
print("Final Amount = ",amt)
        

       