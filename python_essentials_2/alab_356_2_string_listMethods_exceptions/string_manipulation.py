# Task 1: String Manipulation Challenge
# Write a Python script (e.g., string_manipulation.py) that:
# Prompts the user to enter a sentence.
sentence = input("Please enter a sentence: ")
# Converts the entire sentence to uppercase and prints the result.
print("Uppercase:", sentence.upper())
# Prints the sentence in reverse order.
print("Reversed:", sentence[::-1])
# Counts and displays the number of vowels (a, e, i, o, u, regardless of case) present in the sentence.
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
print("Vowel count:", vowel_count)
# Replaces every space in the sentence with a hyphen (-) and prints the modified string.
print("Hyphenated:", sentence.replace(" ", "-"))
# Ensure that each output is clearly labeled (for example, “Uppercase:”, “Reversed:”, etc.).