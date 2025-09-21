#Question No 5
#Average of Three Numbers - 
# Input three numbers and print their average.
#1st method

print("Finding average of three number.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
avg = (num1 + num2 + num3)/3
print("The average of three number is: ", float(avg))

#Second method taking all three input at once through single line code
#Getting all three number as input through split function
#we got an error because we were applying int() before .split().
#and string of numbers cannot be directly converted into integers 
#num1, num2, num3 = int(input("Enter three numbers to find their average (separated by space): \n")).split()

#so using map function to solve this error
print("\nLet's find the average again by taking all input at once.")
num1, num2, num3 = map(int, (input("Enter three numbers (separated by space): ")).split())
avg = (num1 + num2 + num3)/3
print("The average of the given three number is: ", float(avg))