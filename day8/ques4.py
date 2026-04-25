'''4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''
type=input("Subscription = ").lower()
progress=int(input("Progress = "))
score=int(input("Test Score = "))
if type=="premium":
    if progress>=80:
        if score>=70:
            status="Unlock Certificate"
        else:
            status="Retry"
    else: 
        status="first complete course"
elif type=="basic":
    if progress>=50:
        status="limited access"
    else:
        status=="lock content"
else:
    status="deny access"
print("Access Status = ",status)
