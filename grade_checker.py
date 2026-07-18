# Asks the user to input a numeric grade (0-100).
user_grade = int(input("What score did you get on your test? "))

# Uses an if-elif-else structure to convert the numeric grade to a letter grade based on a typical scale:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F 
if user_grade >= 90:
    print("You got an A!") 
elif user_grade >= 80:
    print("You got a B!")
elif user_grade >= 70:
    print("You got a C!")
elif user_grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")

# Includes a final message using a conditional expression (for example, if the grade is passing (A-C) congratulate the user, if it is a D or F, encourage them to try again).
if user_grade >= 70:
    print("Congratulations! You passed!")
else:
    print("Study hard and try again!")
    # print("Sorry, you failed. Study some more try again!" end="\n")
    print("YOU GOT THIS!")