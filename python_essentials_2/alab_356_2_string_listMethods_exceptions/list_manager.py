# Task 2: List Management with Error Handling
# Write a Python script (e.g., list_manager.py) that manages a list of integers using a text-based menu. The menu should offer the following options:
def menu_options():
    print("\n--- LIST MANAGER ---")
# (a) Add a number: Prompt the user for an integer and append it to the list.
    print("a. Add a number")
# (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
    print("b. Remove a number")
# (c) Display the list: Print the current list of numbers.
    print("c. Display the list")
# (d) Quit: Exit the program.
    print("d. Quit")

# Use a loop to continuously display the menu until the user chooses to quit.
def main():
    numbers = []
    
    while True:
        menu_options()
        choice = input("Choose an option (a, b, c, d): ").strip().lower()
        
        if choice == 'a':
            try:
                val = input("Enter an integer to add: ")
                num = int(val)
                numbers.append(num)
                print(f"Successfully added {num}.")
            except ValueError:
                print("Error: Please enter a valid integer.")
                
        elif choice == 'b':
            if not numbers:
                print("The list is currently empty. Nothing to remove.")
                continue
            try:
                val = input(f"Enter index to remove (0 to {len(numbers) - 1}): ")
                index = int(val)
                removed = numbers.pop(index)
                print(f"Successfully removed {removed} from index {index}.")
            except ValueError:
                print("Error: Please enter a valid integer for the index.")
            except IndexError:
                print(f"Error: Index out of range. Valid range is 0 to {len(numbers) - 1}.")
                
        elif choice == 'c':
            print("Current list:", numbers)
            
        elif choice == 'd':
            print("Exiting List Manager. Goodbye!")
            break
            
        else:
            print("Error: Invalid choice. Please select a, b, c, or d.")

if __name__ == "__main__":
    main()
# Implement error handling using try/except:
# Catch errors when a non-integer is entered for the number or index.
# Catch an IndexError if the user provides an invalid index for removal.
# Display clear error messages for any exceptions without terminating the program abruptly.
