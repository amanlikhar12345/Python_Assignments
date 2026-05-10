'''2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.

'''
mark=int(input("enter the marks :"))
grade='A+' if mark>=90 else 'A' if mark>=75  else 'b' if mark>=60  else 'c' if mark>=50 else "Fail" 
print(grade)