'''1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation

'''
age=int(input("Policy Age = "))
amt=int(input("Claim Amount = "))
type=input("Accident Type = ")
s=""
if age>=2:
    if amt<=50000:
        if type=="minor":
            s="approve"
        else:
            s="approve it with inspection"
    elif amt>50000 and amt<200000:
        if type=="major":
            s="approve with investigation"
        else:
            s="reject"
    else:
        status="rejected"
if age<2:
    if type=="minor":
        s="reject"
    else:
        s="pending review"
print("Claim Status = ",s)
