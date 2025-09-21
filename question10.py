#Question No 10
# Salary Calculator
# Input basic salary. Calculate:
# HRA = 20% of basic
# DA = 15% of basic
# Total Salary = Basic + HRA + DA

bs = int(input("Enter basic salary: ")) #bs for basic salary
hra = (20/100) * bs #HRA may be house rent allowance
print("Your HRA allowance which is 20 percent for the basic salary is: ",hra)
da = (15/100) * bs #DA i guess doctor allowance
print("Your DA allowance which is 15 percent for the basic salary is: ",da)
total_salary = bs + hra + da
print("So total salary after including allowances are: ", total_salary)