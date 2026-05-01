'''3.

Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2
'''
num=int(input("Input:"))
f1=-1
f2=1
count=0
sum=0
print("Population Growth: ")
for i in range(1,num+1):
    f=f1+f2
    print(f,end=" ")
    if f>5:
        count+=1
    sum+=f
    f1=f2
    f2=f
print("")
print("Total Population = ",sum)
print("Months with Population > 5 = ",count)