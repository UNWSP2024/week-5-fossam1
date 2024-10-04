# Samuel Foss
# Program 2: Math Quiz
# 10/4/2024

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
def quiz():
    answer = int(input("What is 15 + 9? : "))
    if answer == 24 : print("Congratulations!")
    else : print("The answer is 24!")

quiz()
#Output
#What is 15 + 9? : 24
#Congratulations!

#Process finished with exit code 0
