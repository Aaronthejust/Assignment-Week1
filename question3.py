#Question No 3
#Calculate Compound Interest
#Use the formula:
#CI = P * (1 + R/100)**T - P

# I used int as input intentionally we can also take it as float
p = int(input("Enter Principle Amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time (in years): "))

ci = p * (1 + r/100)**t - p

print("The compound interest for the given data is: ", float(ci))