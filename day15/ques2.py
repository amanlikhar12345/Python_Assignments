'''2.
Fibonacci Series Generator

A learning app helps students understand number patterns. One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

The series starts with:
0 1

Write a program to:

- Read a number n (number of terms)
- Print the Fibonacci series up to n terms using a loop

Input:
7

Output:
0 1 1 2 3 5 8
'''
num=int(input("Input:"))
f1=-1
f2=1
for i in range(1,num+1):
    f=f1+f2
    print(f,end=" ")
    f1=f2
    f2=f