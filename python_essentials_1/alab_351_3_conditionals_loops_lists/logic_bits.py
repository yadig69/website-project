print("-- Logical Operators --")

# ask the user for two boolean inputs
a = input("Enter first boolean (True/False or 1/0): ").strip()
b = input("Enter second boolean (True/False or 1/0): ").strip()

# convert input to actual booleans — handles both "1/0" and "True/False"
a = bool(int(a)) if a in ("0", "1") else a.lower() == "true"
b = bool(int(b)) if b in ("0", "1") else b.lower() == "true"

print(f"a = {a}, b = {b}")

# and: returns True only if BOTH a and b are True
print(f"a and b  : {a and b}")

# or: returns True if AT LEAST ONE of a or b is True
print(f"a or b   : {a or b}")

# not: flips the boolean — True becomes False, False becomes True
print(f"not a    : {not a}")
print(f"not b    : {not b}")

print("\n-- Bitwise Operators --")

# two small integers to demonstrate bitwise operations
x, y = 5, 3  # 5 = 0b101, 3 = 0b011
print(f"x = {x} ({bin(x)}), y = {y} ({bin(y)})")

# & AND: compares each bit — result bit is 1 only if BOTH bits are 1
# 101 & 011 = 001 (only the last bit matches)
print(f"x & y  (AND) : {x & y}  -> {bin(x & y)}")

# | OR: result bit is 1 if AT LEAST ONE bit is 1
# 101 | 011 = 111
print(f"x | y  (OR)  : {x | y}  -> {bin(x | y)}")

# ^ XOR: result bit is 1 only if the bits are DIFFERENT
# 101 ^ 011 = 110
print(f"x ^ y  (XOR) : {x ^ y}  -> {bin(x ^ y)}")

# ~ NOT: flips all bits — result is -(x + 1) due to two's complement
print(f"~x     (NOT) : {~x}  -> {bin(~x)}")

# << LEFT SHIFT: shifts bits left by 1 — equivalent to multiplying by 2
# 101 << 1 = 1010 (5 * 2 = 10)
print(f"x << 1 (LEFT SHIFT)  : {x << 1}  -> {bin(x << 1)}")

# >> RIGHT SHIFT: shifts bits right by 1 — equivalent to dividing by 2
# 101 >> 1 = 10 (5 // 2 = 2)
print(f"x >> 1 (RIGHT SHIFT) : {x >> 1}  -> {bin(x >> 1)}")
