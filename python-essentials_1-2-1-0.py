print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
print()
print()
# 2.1.9 using multiple arguments
# The arguments are separated by commas. We've surrounded them with spaces to make them more visible, but it's not really necessary, and we won't be doing it anymore.
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
print()
# 2.1.10 Positional arguments
# 2.1.11 Keyword arguments
# a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
# any keyword arguments have to be put after the last positional argument (this is very important)
# In our example, we have made use of the end keyword argument, and set it to a string containing one space.
print("My name is", "Python.", end=" ")
print("Monty Python.")
print()
print("My name is ", end="")
print("Monty Python.")
print()
# We said previously that the print() function separates its outputted arguments with spaces. This behavior can be changed, too.
# The keyword argument that can do this is named sep (as in separator).
# Look at the code in the editor, and run it.

print("My", "name", "is", "Monty", "Python.", sep="-")
# The print() function now uses a dash, instead of a space, to separate the outputted arguments.
# Note: th sep argument's value can be a string of any length.
print()
print("My", "name", "is", sep="_", end="*")
print()
print("Monty", "Python.", sep="*", end="*\n")