'''Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
run=int(input("enter the total runs"))
over=float(input("enter the over"))
overs=over//1
balls=(over*10)%10
print(overs)
print(balls)
total_balls=(6*overs)+balls
run_rate=run/over
x=round(run_rate,2)


print(f"Total Balls = {total_balls}\nRun Rate = {x}")
