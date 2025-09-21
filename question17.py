# Question 17:
# Convert Minutes to Hours and Minutes
# Input number of minutes and convert to hours and remaining minutes.
# Example: 130 minutes → 2 hours 10 minutes

minutes = int(input("Enter the time in minutes: "))
hour = minutes // 60 #floor division to take the quotient
rem_minutes = minutes % 60  #modulas so if remaining minutes are left
print("The time in hour is: ",int(hour),"hours and", int(rem_minutes), "minutes")