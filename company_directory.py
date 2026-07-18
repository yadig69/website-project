# create a simple contact directory program called phone_book
phone_book = {
    "Bob": "555-1234",
    "Alice": "555-9876"
}
# Look up and print Bob's phone number using his name as the key.
print("Bob's phone number:", phone_book["Bob"])
# Alice changed her number. Update her phone number in the dictionary to "555-0000".
print()
print("Alice old number:", phone_book["Alice"])
phone_book["Alice"] = "555-0000"
print()
print("Alice updated number:", phone_book["Alice"])
# A new person joined. Add "David" to the dictionary with the phone number "555-4321".
phone_book["David"] = "555-4321"

print(phone_book)