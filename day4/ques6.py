'''Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
'''
data=int(input("enter the data into GB"))
mb=1024*data
kb=1024*mb
print(f"In MB = {mb}\nIn KB ={kb} ")