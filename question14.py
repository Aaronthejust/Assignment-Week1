# Question No 14
# Percentage of Correct Answers
# Input total questions and correct answers, and calculate the percentage score.
#for while loop initialization first
tot_q = 0
cor_ans = 0
#check loop to validate condition first so user input correct data
while tot_q <= 0 or cor_ans <= 0 or tot_q < cor_ans:
    tot_q = int(input("Enter total no of question: ")) #tot_q for total question
    print("Total Questions are: ",int(tot_q))
    cor_ans = int(input("Correct answers: "))
    print("Correct answers are: ",cor_ans)
    if tot_q <= 0:
        print("Total questions should be greater than zero.")
    elif cor_ans <= 0:
        print("Correct answer should be greater than zero.")
    elif tot_q < cor_ans:
        print("Total questions should be greater than or equal to correct answers")    
    

percentage = (cor_ans/tot_q) * 100
#using f string as it does not need to typecasting or conversion of datatypes
print(f"The percentage of correct answers is: {percentage: .2f}%")
