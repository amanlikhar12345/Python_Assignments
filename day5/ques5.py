'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
'''
name=input("Enter username: ")
password=input("Enter password: ")
password_len=len(password)
if name=="admin" and password_len>=8:
    print("Valid user\nStrong password")
