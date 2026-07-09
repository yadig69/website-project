# Ask the user for their age and convert the input to an integer
age = int(input("How old are you? "))

# Check the age and print the corresponding message
if age < 18:
    print("access denied. too young!")
elif 18 <= age <= 20:
    print("you can come in, but no drinking!")
else:
    print("welcome in! enjoy your night")