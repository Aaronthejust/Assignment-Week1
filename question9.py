#Question No 9
# Total Marks and Percentage
# Input marks of 5 subjects. Print:
# Total marks
#  Percentage
#  Average

#as we are taking multiple inputs so using map for int function and iterable which is input here so that we take multiple input using single input fucntion
sub1, sub2, sub3, sub4, sub5 = map(int, input("Enter obtained number of 5 subjects(separated by space): ").split())
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
print("Total Marks in 5 subjects are: ", total_marks)
#let's assume each subject has 100 marks
percentage = (total_marks/500) *100
print("Percentage of total marks is: ",percentage,"%")
avg = total_marks/5
print("Average of marks in 5 subjects is: ",avg)


