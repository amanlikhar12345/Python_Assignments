'''6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.

ch=input("enter the character : ")

print("Alphabet" if ch.isalpha() else "Digit" if ch.isdigit() else "Special Character")'''




num=int(input("enter the number "))
m=0
d=0
if num>=1000:
    rem=num%1000
    m=num//1000
    while m>0:
        print("m",end="")
        m-=1

    if rem>=500:
        rem1=rem%500
        d=rem//500
        while d>0:
            print("d",end="")
            d-=1

        