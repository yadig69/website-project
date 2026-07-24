# The corrupted satellite data feed
satellite_feed = [
    "72-69-76-76-79",       # Encrypted Word 1 (ASCII decimal codes)
    "87-79-82-76-68",       # Encrypted Word 2 (ASCII decimal codes)
    42,                     # Global positioning float code (Corrupted data!)
    "  _sYstEm_oNlInE_  ",  # System status string
    "0"                     # Battery critical override multiplier
]


# Task 1: Characters & Strings vs. Computers
print(satellite_feed[0])
print(satellite_feed[1])

def decrypt_message(coded_string):
    number_strings = coded_string.split('-')
    decoded_word = "".join(chr(int(num)) for num in number_strings)
    return decoded_word

print(" -- Task 1 results --" )
print(decrypt_message(satellite_feed[0]))
print(decrypt_message(satellite_feed[1]))
print(decrypt_message(satellite_feed[0]) + ' ' + decrypt_message(satellite_feed[1]))

# Task 2: Strings in Action (The Cleanup)
messy_word = satellite_feed[3]
cleaned_word = messy_word.strip().replace("_", " ").strip().lower()
print(" -- Task 2 results --")
print(f"Cleaned up: {cleaned_word}\n")

# Task 3: The Anatomy of Exceptions (The Crash Test)
for item in satellite_feed:
    if isinstance(item, str) and '-' in item:
        print(decrypt_message(item))
    elif not isinstance(item, str):
        print(f"Cannot decode {item} because it is not a string.")

# Task 4: Useful Exceptions (The Bulletproof Shield)
print(" -- Task 4 results --")
for item in satellite_feed:
    print(f"\nProcessing item: {repr(item)}")
    try:
        decoded = decrypt_message(item)
        print(f"Decoded: {decoded}")
    except AttributeError:
        print("[SYSTEM WARNING]: Skipped corrupted non-string data.")
        continue

    try:
        numeric_value = int(item)
        result = 100 / numeric_value
        print(f"-> Division calculation results (100 / {numeric_value}) = {result}")
    except ZeroDivisionError:
        print(f"-> [SYSTEM WARNING]: Cannot divide by zero override.")
    except (ValueError, TypeError):
        pass
