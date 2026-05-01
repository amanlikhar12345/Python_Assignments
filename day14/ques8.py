'''8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
'''
amt=int(input("Input:"))
note=0
for i in range(1,amt//100+1):
    note+=1
print("Notes = ",note)