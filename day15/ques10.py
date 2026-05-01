'''10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700'''

n=int(input("enter the n house"))
sum=0
high=0
for i in range(1,n+1):
    unit=int(input(f"enter the unit of {i} house"))
    bill=0
    if unit<=100:
        bill=5*unit
        if unit<50:
            bill-=100
    elif unit>100 and unit<200:
        unit-=100
        bill=500+unit*7
    else:
        unit-=200
        bill=1200+unit*10
        if bill>2000:
            sur=(bill*10)//100
            bill+=sur

    if high<bill:
        high=bill
    print(f"house {i} bill = {bill}")
    
    sum+=bill
print("Highest Bill = ",high)
print("Total Collection = ",sum)