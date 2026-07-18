# Goal: Practice iterating through data with a for loop and building a new list on the fly.
# Your Mission
# Create a list of numbers from 1 to 20.
numbers = list(range(1, 20))
# Create a second, empty list called multiples_of_three.
multiples_of_three = []
# Use a for loop to look at every number in your first list. If a number is perfectly divisible by 3, append it to your second list.
for num in numbers:
    if num % 2 == 0:
        multiples_of_three.append(num)
# Print the final multiples_of_three list.
print(multiples_of_three)

# Hint: To check if a number is perfectly divisible by something, use the modulo operator (%), which calculates the remainder of a division. If num % 3 == 0, it’s a multiple of 3!
print(5 == '5')


