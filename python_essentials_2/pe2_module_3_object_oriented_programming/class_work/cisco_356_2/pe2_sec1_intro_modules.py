# Note: print the value of sin(½π)
import math
print(math.sin(math.pi/2))

# Note: qualify the names of pi and sin with the name of its originating module:
math.pi
math.sin

# Note: import only the names of pi and sin into the local namespace:
from math import pi, sin
# Note: how the two namespaces (yours and the module's one) can coexist.

import math

def sin(x):
    
    if 2 * x == pi:
        return 0.99999999
    else:
       return None
   
pi = 3.14
   
print(sin(pi/2))
print(math.sin(math.pi/2))

# Note: The instruction has this effect:

# Note: the listed entities (and only those ones) are imported from the indicated module;
# Note: the names of the imported entities are accessible without qualification.
# Note: no other entities are imported. Moreover, you cannot import additional entities using a qualification - a line like this one:


print(math.e)
# Note: will cause an error (e is Euler's number: 2.71828...)

# * rewrite the previous script to incorporate the new technique.
# line 1: carry out the selective import;
from math import sin, pi
# line 3: make use of the imported entities and get the expected result (1.0)
print(sin(pi/2))
# # lines 5 through 12: redefine the meaning of pi and sin - in effect, they supersede the original (imported) definitions within the code's namespace;
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
# line 15: get 0.99999999, which confirms our conclusions.
print(sin(pi / 2))


# Let's do another test. Look at the code below:
#Here, we've reversed the sequence of the code's operations:
#lines 1 through 8: define our own pi and sin;
pi = 3.14

#line 11: make use of them (0.99999999 appears on the screen)
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))

#line 13: carry out the import - the imported symbols supersede their previous #definitions within the namespace;
from math import sin, pi
#line 15: get 1.0 as a result.
print(sin(pi / 2))

#^ 1.1.7 The as keyword

# If you use the import module variant and you don't like a particular module's name (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) you can give it any name you like - this is called aliasing.

# # Aliasing causes the module to be identified under a different name than the original. This may shorten the qualified names, too.

# # Creating an alias is done together with importing the module, and demands the following form of the import instruction:
#
# from module import name as alias
# import module as alias

# Note: Both of these forms make the module's entities available under a different name, which is much easier to use in the code.

# Note: The "module" identifies the original module's name while the "alias" is the name you wish to use instead of the original.

# Note: as is a keyword.

# ^ 1.1.8 Aliasing
# Note: If you need to change the word math, you can introduce your own name, just like in the example:

import math as m
print(m.sin(m.pi / 2))


#^ 1.1.10 SECTION QUIZ
#? Question 1: You want to invoke the function make_money() contained in the module named mint. Your code begins with the following line:
#? import mint
#? What is the proper form of the function's invocation?
#& mint.make_money()
#& print(mint.make_money())

#? Question 2: You want to invoke the function make_money() contained in the module named mint. Your code begins with the following line:
#? from mint import make_money
#? What is the proper form of the function's invocation?
#& make_money()

#? Question 3: You've written a function named make_money on your own. You need to import a function of the same name from the mint module and don't want to rename any of your previously defined names. Which variant of the import statement may help you with the issue?
#& from mint import make_money as create_the_bag

#? Question 4: What form of the make_money function invocation is valid if your code starts with the following line?
#? from mint import *
#& make_money()

