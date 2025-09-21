#Question No 7
#Distribute Items Equally - You have n candies and k students.
#Write a program to find:
#how many candies each student gets
#how many are left

n = int(input("Enter number of candies: "))
k = int(input("Enter number of students: "))

#let take out the infinity issue

if k == 0:
    print("No student to distribute candies.")
elif n < k:
       print("The No of candies are less than the no of students to distribute equally.\nEnter candies equal to or greater than No of students.")
else:
    no_of_candies = n // k  #using // to get the quotient number
    left_candies = n % k    #using % to get the remainder
    print("The no of candies each student got: ", no_of_candies)
    print("The left over candies are: ", left_candies)

#we can also solve this problem through loop
#until and unless the condition is not true
#the loop will ask again and again for correct input

#initialize first

n = 0
k = 0

while n <= 0 or k <= 0 or n < k :
     n = int(input("\nEnter number of candies: "))
     k = int(input("Enter number of students: ")) 
     
     if n <= 0:
          print("Candies must be greater than zero")
     elif k <= 0 :
          print("Students number must be greater than zero.")
     elif n < k:
          print("Candies must be greater than number of students.")
     


#after getting valid entries now distributing the candies

num_of_candies = n // k
left_over_candies = n % k
print("The number of candies each student got: ", num_of_candies)
print("The number of left over candies: ", left_over_candies) 
          
            