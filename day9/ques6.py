'''6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
'''
amt=int(input("Amount = "))
loca=input("Location = ").lower()
device=input("Device = ").lower()
tran=int(input("Transactions = "))
if amt>=50000:
    if loca=="international":
        if device=="new":
            if tran>3:
                risk="High Risk (Blocked)"
            else:
                risk="Medium Risk"
        else:
            risk="Medium Risk"
    else:
        if tran>5:
            risk="Medium Risk"
        else:
            risk="Low Risk"
else:
    if active==True:
        if device=="new":
            risk="Medium Risk"
        else:
            risk="Low Risk"
    else:
        risk="safe"
print("Risk Level = ",risk)