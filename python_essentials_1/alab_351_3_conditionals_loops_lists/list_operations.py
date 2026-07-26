# Write a script list_operations.py that:
print("-- list operations --")

# Creates a list of at least 5 integers (you can choose them arbitrarily or ask the user to input numbers to populate the list).
my_list = [int(x.strip()) for x in input("enter 5 numbers separated by commas or spaces: ").replace(",", " ").split()]
# Prints the original list.
print(f"my original list is: {my_list}")
# Uses the built-in sorted() function to print a sorted version of the list without modifying the original list.
print(f"my sorted list is: {sorted(my_list)}")
# Uses the list’s .sort() method to sort the list in place, then prints the list to show it is now sorted.
my_list.sort()
print(f"my sorted list is: {my_list}")
# Adds a new element to the list (append an integer), then prints the updated list.
my_list.append(24)
print(f"my list with appended number is: {my_list}")
# Removes an element from the list (you can remove by value or index), then prints the list again.
my_list.remove(24)
print(f"my list with number unpended is: {my_list}")
# Uses the reverse() method to reverse the list, then prints the reversed list.
my_list.reverse()
print(f"my list reversed is: {my_list}")
# Each step should be clearly separated and labeled in the output, for example by printing a message like "Original list:", "Sorted list:", etc.
