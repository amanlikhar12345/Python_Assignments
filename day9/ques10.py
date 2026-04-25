'''10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected'''

age=int(input("Age = "))
bmi=int(input("BMI = "))
run=int(input("Running Time = "))
medical=input("Medical = ").lower()

if age>=18 and age<=25:
    if bmi>=18 and bmi<=25:
        if run<=15:
            if medical=="fit":
                status="selected"
            else:
                status="medical reject"   
        else:
            if run>15:
                status="physical fail"
    else:
        status="BMI fail"
elif age>=26 and age<=30:
    if run<=14 and medical=="fit":
        status="conditional selection"
    else:
        status="Reject"
else:
    status="not eligible"
print("Selection Status = ",status)