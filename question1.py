#Question No 1
#Write a program that converts a temperature from Celsius 
# to Fahrenheit. (Formula: Fahrenheit =(Celsius * 9/5) + 32)

#Taking celcius as input from use

celsius = int(input("\nEnter temperature in Celsius to convert into Fahrenheit: "))
fahrenheit = (celsius * 9/5) + 32 #using formula
print("\nThe temperature in Fahrenheit is: ", float(fahrenheit)) #taking output as float
