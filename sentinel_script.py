# Goal: Use a while loop to keep a program running until a specific logical condition is met.
# Your Mission
# Write a program that continuously asks the user to input a password.
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
# The loop should only stop if the user types "python123" OR if they have guessed incorrectly 3 times (intruder alert!).
    if password == "python123":
# If they get it right, print: "Access granted."
       print("Access granted.", end="")
       break
    else:
        attempts += 1
        print("Incorrect password.", end="")
# If they run out of attempts, print: "Account locked. Try again later."
if attempts == max_attempts:
    print("Account locked. Try again later.", end="")

