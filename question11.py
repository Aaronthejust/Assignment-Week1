#Question No 11
# Age in Months and Days
# Input your age in years. Calculate and print age in:
# Months
# Days (approximate)

age = float(input("Enter your age in years: "))
age_in_months = age * 12 #since each year has 12 months
print("Your age in months is: ", int(age_in_months),"months")
age_in_days = age * 365  #as each year has 365 days
print("Your age in days is (aproximately): ", int(age_in_days),"days")