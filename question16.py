# Question No 16:
# Calculate Body Mass Index (BMI)
# Input weight (kg) and height (m), then calculate:
# BMI = weight / (height ** 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))
bmi = weight/(height**2)
print(f"Your BMI is: {bmi: .2f}")