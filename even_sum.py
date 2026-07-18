even_sum = 0
# Uses a for loop to iterate through the numbers 1 to 50.
for number in range(1, 51):
# Calculates the sum of all even numbers in that range.
    # Determines if the current number is even.
    if number % 2 == 0:
        even_sum += number
# Prints the result as: "The sum of even numbers from 1 to 50 is X." (where X is the calculated sum).
print(f"The sum of even numbers from 1 to 50 is {even_sum}.")


# Next, modify the script to perform the same task using a while loop instead of a for loop. You can include this in the same file or as a separate block of code within the file, and print the result again to verify it matches. Comment on whether both loop versions produce the same result and which approach you find clearer.