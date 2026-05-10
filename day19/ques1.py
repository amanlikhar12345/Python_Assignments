'''1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''


while True:
    print("Menu Option :")
    print("1 → Check Prime Number")
    print("2 → Check Palindrome Number")
    print("3 → Reverse a Number")
    print("4 → Count Digits")
    print("5 → Exit")
    ch=int(input("Enter your choice: "))
    
    match ch:
        case 1:
            num=int(input("Enter the Number :"))
            if num==1:
                print("1 is Not prime number")
            else :
                for i in range(2,num):
                    if num%i==0:
                        print("Not Prime Number")
                        break
                else:
                    print(f"{num} is a Prime Number")
          
        case 2:
            num=int(input("Enter the Number :"))  
            num1=num
            rev=0
            while num>0:
                rem=num%10
                num=num//10
                rev=(rev*10)+rem

            if num1==rev:
                print(f"{rev} is a Palindrome Number")
            else:
                print(f"{num1} is not a Palindrome Number")

        case 3:
            num=int(input("Enter the Number :"))  
            num1=num
            rev=0
            while num>0:
                rem=num%10
                num=num//10
                rev=(rev*10)+rem
            print("reverse number is :",rev)
 
        case 4: 
            num=int(input("Enter the Number :")) 
            count=0
            if num==0:
               count+=1
            while num>0:
                num=num//10
                count+=1
            print("Total digits: ",count)
  

        case 5:
              break
 
        case _ :
            print("Invalid choice. Please try again.")
                    