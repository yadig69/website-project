# Requirements
# Your Contact Book application should support the following features:

# Add a New Contact: Prompt the user for a name and phone number. Store this contact in the contact list (or dictionary). Ensure that a name can only exist once (if the user tries to add a name that already exists, print a message and do not duplicate the entry).
# View All Contacts: Display a list of all contacts currently stored, showing each contact’s name and phone number. If there are no contacts, print a message saying the contact list is empty.
# Search for a Contact: Ask the user for a name (or part of a name) to search. Display any contacts that match (this can be an exact match or, for an extra challenge, allow partial matches). If no match is found, inform the user.
# Delete a Contact: Ask the user for the name of the contact to delete. If the contact exists, remove it from the list and confirm deletion. If it doesn’t exist, print a message stating so.
# Exit: Exit the program.
# The program should use a loop to show the menu after each action (except exit). The menu can be text-

phone_book = {
    "Bob": "555-1234",
    "Alice": "555-9876"
}

while True:
    # Display the interactive menu
    print("\n--- CONTACT MENU ---")
    print("1.Look up a contact")
    print("2.Add or update a contact")
    print("3.Delete a contact")
    print("4.View all contacts")
    print("5.Exit")
    
    choice = input("Enter your choice (1 - 4) ").strip()
    
    # Option 1: Search / Look up a contact
    if choice == "1":
        search_name = input("Enter the name you want to search for: ").strip()
        
        # check if name exist as a key in the directory
        if search_name in phone_book:
            print(f"{search_name}'s phone number is: {phone_book[search_name]}")
        else:
            print(f"Sorry, {search_name} is not in the phone book.")
           
        # Option 2: add or Update a contact
    elif choice == "2":
        name = input("Enter the name: ").strip()
        phone = input("Enter the phone number: ").strip()

            # check if name exist as a key in the directory
        if name in phone_book:
            print(f"{name} is already in the phone book.")
            update = input("Do you want to update the number? (yes/no): ").strip().lower()
            if update == "yes":
                phone_book[name] = phone
                print(f"{name}'s phone number has been updated to {phone}")
            else:
                print("Update canceled.")
        else:
            phone_book[name] = phone
            print(f"{name} has been added to the phone book.")
            
    # Option 3: delete a contact
    elif choice == "3":
        name = input("Enter the name of the contact to delete: ").strip()

        # check if name exist as a key in the directory
        if name in phone_book:
            del phone_book[name]
            print(f"{name} has been deleted from the phone book.")
        else:
            print(f"Sorry, {name} is not in the phone book.")
            
    # Option 4: View all contacts
    elif choice == "4":
        if phone_book:
            print("\n--- ALL CONTACTS ---")
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("\nThe phone book is empty.")
            
    # Option 5: Exit
    elif choice == "5":
        print("Exiting the contact book. Goodbye!")
        break