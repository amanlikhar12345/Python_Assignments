'''2.
 Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!
'''

while True:
    print("Menu Options:")
    print()
    print()
    print("1 → Enter Basic Salary")
    print("2 → Calculate HRA (20%) and DA (10%)")
    print("3 → Calculate Net Salary")
    print("4 → Tax Deduction")
    print("* Salary > 50000 → 10% tax")
    print("5 → Display Salary Slip")
    print("6 → Exit")
    print()
    print()
    ch=int(input("Enter your choice: "))
    global sal
    sal=0
    
    match ch:
        case 1:
            sal=int(input("Enter Basic Salary: "))
            print("Basic Salary recorded successfully")

        case 2:
            if sal==0:
                print("Please enter basic salary first")
          
            else:
                hra=(sal*20)//100
                da=(sal*10)//100
                print("HRA: ",hra)
                print("DA: ",da)

        case 3:
            if sal==0:
                print("Please enter basic salary first")
                
            else:
                net=hra+da+sal
                print("Net Salary (before tax): ",net) 

        case 4:
            if sal==None:
                print("Please enter basic salary first")
                break
            if sal>50000:
                tax=(net*5)//100
            else :
                tax=(net*3)//100
            print("Tax Deduction: ",tax)

        case 5:
            final=net-tax
            print("Basic Salary: ",sal)
            print("HRA: ",hra)
            print("DA: ",da)
            print("Net Salary: ",net)
            print("Tax: ",tax)
            print("Final Salary: ",final)

        case 6:
             break           

