"""

 _______ _                        ______ _                          ______             _                                                     
( ______) |                  _   / _____) |                  _     (_____ \        _  | |                                                    
| |     | |__  _____ _____ _| |_( (____ | |__  _____ _____ _| |_    _____) )   _ _| |_| |__   ___  ____                                      
| |     |  _ \| ___ (____ (_   _)\____ \|  _ \| ___ | ___ (_   _)  |  ____/ | | (_   _)  _ \ / _ \|  _ \                                     
| |_____| | | | ____/ ___ | | |_ _____) ) | | | ____| ____| | |_   | |    | |_| | | |_| | | | |_| | | | |                                    
 \______)_| |_|_____)_____|  \__|______/|_| |_|_____)_____)  \__)  |_|     \__  |  \__)_| |_|\___/|_| |_|                                    
                                                                           (____/                                                             
 
                          __   ___     __         ___          __      __  ___  __       ___         __                                               
               |\/|  /\  |  \ |__     |__) \ /     |  |  |\/| /  \    /__`  |  |__)  /\   |  | |\ | / _`                                              
               |  | /~~\ |__/ |___    |__)  |      |  |  |  | \__/    .__/  |  |  \ /~~\  |  | | \| \__>                                              
                                                                                                                                        



Thanks to: 

https://github.com/trekhleb/learn-python
https://learnxinyminutes.com/

"""





########################################################################################################
## 0. Index
########################################################################################################

# 1. Primitive Datatypes and Operators
# 1.1 Type casting
#
# 2. Variables and Collections
# 2.1 Dictionaries
# 2.2 Sets
# 2.3 Named Tuples
# 2.4 Collections Counter
#
# 3. Control Flow and Iterables
# 3.1 Python specific control and flow
#
# 4. Functions
# 4.1 Lambda functions
#
# 5. Modules
#
# 6. Classes
#- 6.1 Inheritance
#- 6.2 Multiple Inheritance
#
# 7. Lazy evaluation
#
# 8. Exceptions
# 

# APPENDIX
# A. Hanze week 1  (May contain errors)
# B. Hanze week 2  (May contain errors)
# C. Hanze week 3  (May contain errors)
# D. Hanze week 4  (May contain errors)
# E. Proef toets








########################################################################################################
## 1. Primitive Datatypes and Operators
########################################################################################################

"""
NUMBERS         123, 4.1415, 3+4j, 0b111, Decimal(), Fraction()
STRING          'spam', "Bob's", b'a\x01c', u'sp\xc4m'
LIST            [1, 2, 3], list(range(10))
DICTIONARIES    {1, "een"}, {"een", 1}, dict(hours=10)
TUPLES          (1,2), tupel('spam'), namedtuple                    # Please note that (1) is not a tuple but (1,) is
FILES           open('jammer.txt')
SETS            set('abc'), {'a', 'b', 'c'}                         # Every item will be unique
CORE TYPES      Booleans, types, None
PROGRAM TYPES   Fucntions, modules, classes
"""


# You have numbers
3  # => 3

# Math is what you would expect
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Result of integer division truncated down both for positive and negative.
5 // 3       # => 1
5.0 // 3.0   # => 1.0 # works on floats too
-5 // 3      # => -2
-5.0 // 3.0  # => -2.0

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# Modulo operation
7 % 3  # => 1

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Boolean values are primitives (Note: the capitalization)
True
False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True


# Note using Bool operators with ints
# False is 0 and True is 1
# Don't mix up with bool(ints) and bitwise and/or (&,|)
0 and 2     # => 0
-5 or 0     # => -5
0 == False  # => True
2 == True   # => False
1 == True   # => True
-5 != False != True #=> True

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparisons can be chained!
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal


# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too! But try not to do this.
"Hello " + "world!"  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"    # => "Hello world!"

# A string can be treated like a list of characters
"This is a string"[0]  # => 'T'

# You can find the length of a string
len("This is a string")  # => 16

# .format can be used to format strings, like this:
"{} can be {}".format("Strings", "interpolated")  # => "Strings can be interpolated"

# You can repeat the formatting arguments to save some typing.
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")  # => "Bob wants to eat lasagna"

# If your Python 3 code also needs to run on Python 2.5 and below, you can also
# still use the old style of formatting:
"%s can be %s the %s way" % ("Strings", "interpolated", "old")  # => "Strings can be interpolated the old way"

# You can also format using f-strings or formatted string literals (in Python 3.6+)
name = "Reiko"
f"She said her name is {name}." # => "She said her name is Reiko"
# You can basically put any Python statement inside the braces and it will be output in the string.
f"{name} is {len(name)} characters long."


# None is an object
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None  # => False
None is None   # => True

# None, 0, and empty strings/lists/dicts/tuples all evaluate to False.
# All other values are True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
bool(())  # => False








####################################################
## 1.1 Type casting
####################################################


# - int() - constructs an integer number from an integer literal, a float literal (by rounding down
#           to the previous whole number) literal, or a string literal (providing the string represents a
#           whole number)

def test_type_casting_to_integer():
    """Type casting to integer"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int('3') == 3


# - float() - constructs a float number from an integer literal, a float literal or a string literal
#             (providing the string represents a float or an integer)

def test_type_casting_to_float():
    """Type casting to float"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


# - str() - constructs a string from a wide variety of data types, including strings, integer
#           literals and float literals

def test_type_casting_to_string():
    """Type casting to string"""

    assert str("s1") == 's1'
    assert str(2) == '2'














########################################################################################################
## 2. Variables and Collections
########################################################################################################

"""

>>> False == 0
True
>>> True == 1
True


Empty objects -- any nonzero number or nonempty object is True

None
0 and 0.0
[ ] an empty list
( ) an empty tuple
{ } an empty dict
' ' an empty string
set() an empty set 

"""

# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!

# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlier versions of Python, input() method was named as raw_input()

# There are no declarations, only assignments.
# Convention is to use lower_case_with_underscores
some_var = 5
some_var  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var  # Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

# no ++ operator
i = 1
i += 1

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # => [2, 4]
# Omit the beginning and return the list
li[2:]    # => [4, 3]
# Omit the end and return the list
li[:3]    # => [1, 2, 4]
# Select every second entry
li[::2]   # =>[1, 4]
# Return a reversed copy of the list
li[::-1]  # => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 6


# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4







####################################################
## 2.1 Dictionaries
####################################################

# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - Dictionary key
# ordering is not guaranteed. Your results might not match this exactly.
list(filled_dict.keys())  # => ["three", "two", "one"]


# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]


# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}













####################################################
## 2.2 Sets
####################################################

# Sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False



"""Set methods"""
fruits_set = {"apple", "banana", "cherry"}

# You may check if the item is in set by using "in" statement
"apple" in fruits_set
"pineapple" not in fruits_set

# Use the len() method to return the number of items.
len(fruits_set) == 3

# You can use the add() object method to add an item.
fruits_set.add("pineapple")
"pineapple" in fruits_set
len(fruits_set) == 4

# Use remove() method to remove an item.
fruits_set.remove("pineapple")
"pineapple" not in fruits_set
len(fruits_set) == 3

# Demonstrate set operations on unique letters from two word:
first_char_set = set('abracadabra')
second_char_set = set('alacazam')

first_char_set == {'a', 'r', 'b', 'c', 'd'}  # unique letters in first word
second_char_set == {'a', 'l', 'c', 'z', 'm'}  # unique letters in second word

# Letters in first word but not in second.
first_char_set - second_char_set == {'r', 'b', 'd'}

# Letters in first word or second word or both.
first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# Common letters in both words.
first_char_set & second_char_set == {'a', 'c'}

# Letters in first or second word but not both.
first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

# Similarly to list comprehensions, set comprehensions are also supported:
word = {char for char in 'abracadabra' if char not in 'abc'}
word == {'r', 'd'}





####################################################
## 2.3 Named Tuples
####################################################

from collections import namedtuple
Card = namedtuple("Card", "rank suit")
first = Card("A", "spades")
second = Card ("7", "diamonds")
# >>> first
# Card(rank="A", suit="spades")
# >>> first.rank
# "A"
# >>> first.suit
# "spades"





####################################################
## 2.4 Collections Counter
####################################################

from collections import Counter
counter = Counter('abracadabra')
# >>> counter
# Counter({'a': 5, 'b': 2, 'r': 2, ...})






########################################################################################################
## 3. Control Flow and Iterables
########################################################################################################

# Let's just make a variable
some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")


"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)
"""

While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
next(our_iterator)  # => "one"

# It maintains state as we iterate.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
next(our_iterator)  # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys())  # => Returns ["one", "two", "three"]









####################################################
## 3.1 Python specific control and flow
####################################################


# any and all

any([False, False, True])   # True
all([False, False, True])   # False

any (spyname == "X" for spyname in "I am mr X")   # True



# enumerate

for (index, item) in enumerate("spam"):
    print(item, " = ", index)

# s  =  0
# p  =  1
# a  =  2
# m  =  3



# map

def square(n):
    return n*n

lis = list(range(5))
# [0,1,2,3,4]

map(square, lis)
# [0,1,4,9,16]



# List comprehension

[x*x for x in list(range(5))]
# [0,1,4,9,16]





########################################################################################################
## 4. Functions
########################################################################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.

# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again parenthesis have been excluded but can be included.

# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print(x)   # => 43

def set_global_x(num):
    global x
    print(x)   # => 5
    x = num    # global var x is now set to 6
    print(x)   # => 6

set_x(43)
set_global_x(6)







####################################################
## 4.1 Lambda functions
####################################################

# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



lis = [(1, 'a'), (3, 'c'), (5, 'e'), (-1, 'z')]
min(lis, key=lambda x: x[0])   # (-1, 'z')
min(lis, key=lambda x: x[1])   # (1, 'a')

















########################################################################################################
## 5. Modules
########################################################################################################

# You can import modules
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.
















########################################################################################################
## 6. Classes
########################################################################################################

"""
class method is available in all subclasses
class method receives the class itself instead of an instance
use @classmethod decorator for class method
class method can access class attributes and other methods
why not use a global function ? because it logically belongs to the class


a class is a blueprint for an object; you can create multiple instances of a class (with different initialization)

with inheritance you can reuse code in subclasses


every class has at least one superclass called object
• class ClassName is same as class ClassName(object)
• inherited from object :
• constructor : __init__
• printing : __str__
• compare: __eq__(other)
• dictionary containing the class's namespace: __dict__
• and many more
"""



# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i and j are instances of type Human, or in other words: they are Human objects

    # Call our class method
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())            # => "*grunt*"
    
    # Cannot call static method with instance of object 
    # because i.grunt() will automatically put "self" (the object i) as an argument
    print(i.grunt())                # => TypeError: grunt() takes 0 positional arguments but 1 was given
                                    
    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError














####################################################
## 6.1 Inheritance
####################################################

# Inheritance allows new child classes to be defined that inherit methods and
# variables from their parent class. 

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits the class variables like
# "species", "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

# To take advantage of modularization by file you could place the classes above in their own files,
# say, human.py

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from human import Human


# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = 'Superhuman'

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # override the sing method
    def sing(self):
        return 'Dun, dun, DUN!'

    # add an additional instance method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # Instance type checks
    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # Get the Method Resolution search Order used by both getattr() and super()
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => Dun, dun, DUN!

    # Calls method from Human
    sup.say('Spoon')            # => Tick: Spoon

    # Call method that exists only in Superhero
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute
    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero
    print('Am I Oscar eligible? ' + str(sup.movie))













####################################################
## 6.2 Multiple Inheritance
####################################################

# Another class definition
# bat.py
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)


# And yet another class definition that inherits from Superhero and Bat
# superhero.py
from superhero import Superhero
from bat import Bat

# Define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)      
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Superhero.__init__(self, 'anonymous', movie=True, 
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__)       # => (<class '__main__.Batman'>, 
                                # => <class 'superhero.Superhero'>, 
                                # => <class 'human.Human'>, 
                                # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say('I agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())          # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)              # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False
















########################################################################################################
## 7. Lazy evaluation
########################################################################################################


# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i



# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break



# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]




# Decorators
# In this example `beg` wraps `say`. If say_please is True then it
# will change the returned message.
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())                 # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(


















########################################################################################################
## 8. Exceptions
########################################################################################################

"""
try/except/else/finally
• try : block of code
• except : catch and handle exceptions
• else : only if no exception applies
• finally : always do this ('cleanup actions')
"""

# try
#   <body>
# except <ExceptionType1>:
#   <handle1>
# except <ExceptionType2>:
#   <handle2>
# except:
#   <handle>
# else:
#   <else>
# finally:
#   <last>



















#########################################################################################################
#########################################################################################################
##                                      __   __   ___       __                                         ##
##                                 /\  |__) |__) |__  |\ | |  \ | \_/                                  ##
##                                /~~\ |    |    |___ | \| |__/ | / \                                  ##
##                                                                                                     ##
#########################################################################################################
#########################################################################################################




########################################################################################################
## A. Hanze week 1
########################################################################################################


import random
import math

# Opgave 1
"""
a)maak een lijst met elementen 2, 3 en 4
b)maak een lijst met elementen 'red', 'green'en 'blue'
c)maak een lijst met elementen3, 4 en 5 waarbij range() wordt gebruikt
d)maak een lijst met elementen'a', 'b', 'c' en 'd
"""
array_a = [2,3,4]
array_b = ['red', 'green', 'blue']
array_c = list(range(3,5+1))
array_d = ['a', 'b', 'c', 'd']



# Opgave 2
L = [30, 1, 2, 1, 0, "hello", "Goodbye"]

L.index(1)                  # 1
L.count(1)                  # 2
len(L)                      # 7
max(L)                      # ERROR
L.append(40)                # L = [30, 1, 2, 1, 0, "hello", "Goodbye". 40]
L.insert(1, 43)             # L = [30, 43, 1, 2, 1, 0, 'hello', 'Goodbye']
L.extend([1, 43])           # L = [30, 1, 2, 1, 0, 'hello', 'Goodbye', 1, 43]
L.remove("hello")           # L = [30, 1, 2, 1, 0, 'Goodbye']
L.pop()                     # L = [30, 1, 2, 1, 0, "hello"]
"Goodbye" in L              # True
L.pop(3)                    # L = [30, 1, 2, 0, "hello", "Goodbye"]
L.sort()                    # ERROR
random.shuffle(L)           # L = [0, 'Goodbye', 'hello', 30, 1, 1, 2]



# Opgave 3
L = ['a', 'b', 'c', 'd', 'e']

L[1 : -3]                   # ['b']
L[-4 : -2]                  # ['b', 'c']
L[:3]                       # ['a', 'b', 'c']
L[:2] + L[2:]               # ['a', 'b', 'c', 'd', 'e']
L[:-1]                      # ['a', 'b', 'c', 'd']
L[::-1]                     # ['e', 'd', 'c', 'b', 'a']  
# a[start:end:step] start through not past end, by step  <-- nice
L[:]                        # ['a', 'b', 'c', 'd', 'e']



# Opgave 4
L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]

L1 + L2                     # [30, 1, 2, 1, 0, 1, 21, 13]
3 * L2                      # [1, 21, 13, 1, 21, 13, 1, 21, 13]
L1 > L2                     # True
[x for x in L1]             # [30, 1, 2, 1, 0]
[x for x in L1 if x in L2]  # [1]



# Opgave 5
""" Gegeven de string s = 'Guido van Rossum'. Converteer s naar L = ['Guido', 'van', 'Rossum']. """

s = 'Guido van Rossum'
l = s.split(" ")            # l = ['Guido', 'van', 'Rossum'].



# Opgave 6
### A
L = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    L[i] = L[i -1]
    print(L)

[1, 1, 3, 4, 5, 6]
[1, 1, 1, 4, 5, 6]
[1, 1, 1, 1, 5, 6]
[1, 1, 1, 1, 1, 6]
[1, 1, 1, 1, 1, 1]

### B
L1 = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
L2 = L1    # shallow copy
L1[0] = 'abc'
print(L1)  # ['abc', 3, 5, 7, 9]
print(L2)  # ['abc', 3, 5, 7, 9] <-- shallow copy

### C
a, b = 0, 1
while b < 10:
    print (b)
    a, b = b, a+b
# 1 1 2 3 5 8



# Opgave 7
palindroom_example1 = "lepel"
palindroom_example2 = "parterretrap"

def is_palindroom(string):
    string= str(string)
    x = 0
    while x < len(string) / 2:
        # print(string[x] + " != " + string[(len(string)-1)-x])
        if (string[x] != string[(len(string)-1)-x]):
            return False
        x += 1
    return True

def is_palindroom_short(string):
    length = len(str(string))
    return str(string)[0:math.ceil(length/2)] == str(string)[math.floor(length/2):length][::-1]

def is_palindroom_evenshorter(string):
    str(string) == str(string)[::-1]
    
is_palindroom("lepel")
is_palindroom("parterretrap")
is_palindroom("test")
is_palindroom("oke")



# Opgave 8
T = int(input("Temperatuur in graden Celsius(-20..10): "))
B = int(input("Windkracht in Beaufort(1..9): "))
G = 13 + 0.62*T  -  14 * B ** 0.24  +  0.47 * T * B ** 0.24
print("Gevoelstemperatuur = ", round(G, 1))



# Opgave 9
l = 3
s = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
for i in range(len(s) - (l-1)):
    if s[i:i+l] == "ATG":
        print(i + (l+1))



# Opgave 10
from sys import stdin

NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24

data = []

for i in range(NUMBER_OF_DAYS):
    data.append([])
    for j in range(NUMBER_OF_HOURS):
        data[i].append([])

# read input using input redirection from a file
for line in stdin:
    if line[0] == '#':
        continue
    L = line.strip().split()
        
print("Gemiddelde temperaturen:")


avg = 0
# find the average daily temperature
for i in range(NUMBER_OF_DAYS):
    avg += data[i]

avg /= len(data)
























########################################################################################################
## B. Hanze week 2
########################################################################################################

import collections
import math

# opgave 1
### A
tup1 = (1,2,3,4,5)
tup2 = (5,)

print(tup1, tup2)

### B
tup = ('xx', 'yy','zz')
for x in tup: print (x)

### C
tup1 = (4, 6, 2, 8, 3, 1)
tup1 = list(tup1)
tup1.insert(2, 100)
tup1 = tuple(tup1)
print(tup1)

tup1 = (4, 6, 2, 8, 3, 1)
tup1 = tup1[:2] + (100,) + tup1[2:]
print(tup1)

### D
tup = ('a', 'b', 'c')
print( "".join(tup) )

### E
L = [5, 10, 7]
print( tuple(L) )

### F
L = [(1,2), (3,4), (8,9)]
print( list(zip(*L)) )

### G
L = [ ("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("y", 3) ]
di = {}
for a, b in L: 
    di.setdefault(a, []).append(b) 
print(di)



# opgave 2
d = {"red":4, "blue":1, "green":14, "yellow":2}

### A
d['red'] = d['blue']        #  d = {"red":1, "blue":1, "green":14, "yellow":2}

### B
d['blue'] += 10             #  d = {"red":4, "blue":11, "green":14, "yellow":2}

### C
d['yellow'] = len(d)        #  d = {"red":4, "blue":1, "green":14, "yellow":4}

### D
d['green'] = {'orange' : 6} #  d = {"red":4, "blue":1, "green":{'orange' : 6}, "yellow":2}

### E
d = dict.fromkeys(d, 0)     #  d = {"red":0, "blue":0, "green":04, "yellow":0}

### F
d.pop('black', None)        #  None  d = {"red":4, "blue":1, "green":14, "yellow":2}

### G
d.get('black', None)        #  None  d = {"red":4, "blue":1, "green":14, "yellow":2}

### H
d.setdefault('black', None) #  None  d = {"red":4, "blue":1, "green":14, "yellow":2, 'black': None}

### I
d = {}                      #  d = {}



# opgave 3
### A
d = {'c':1, 'b':2, 'a':3, 'e':1, 'd':3}
for k in sorted(d):
    print(k, d[k])

### B
D = {'a':1, 'b':2, 'c':3, 'd':1, 'e':3, 'f': 5}
print(set(d))



# opgave 4
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}

### A
print(s1 & s2)

### B
print(s1 ^ s2)

### C
L = [1, 7, 4, 8, 9, 9, 4, 1, 4, 11, 14, 21, 15, 5, 2, 5]
needle = {15, 11}
print(len(needle & set(L)) == len(needle))




# opgave 5
### A
t = "Mooi"
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(list("mooi".upper()))
print([x.capitalize() for x in t])

### B
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print([x for x in t if x.isupper()])



# opgave 6


### A
def unique_list(L):
    return list(set(L))

L = [1,2,3,3,3,3,4,5]
print(unique_list(L))


### B
def even_elements(L):
    return [x for x in L if x % 2 == 0]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_elements(L))


### C
def is_pangram(str):
    return set("abcdefghijklmnopqrstuvwxyz") - set(str.lower()) == set()

print(is_pangram("Filmquiz bracht knappe ex-yogi van de wijs"))




#    opgave 8     #

from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4

#initializing board
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)
#define where the ship isship_

row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)

# here your code :
# -ask the user for a guess
# -if the user's right, the game ends
# -warn if the guess is out of the board
# -warn if the guess was already made
# -if the guess is wrong, mark the point with an X and start again
# -print turn and board again here
    
if turn == NR_GUESSES-1:
    print ("Game Over")



# opgave 9
def devisors(num):
    divs = [1]
    for i in range(2, math.ceil( math.sqrt(num))):
        if num % i == 0:
            divs.append(i)
            divs.append(int(num / i))

    # print(str(num)+"    "+str(divs))
    return divs

def perfect_numbers_until(until):
    perfects = []
    for i in range(2, until +1):
        if sum(devisors(i)) == i:
            perfects.append(i)

    return perfects



print(perfect_numbers_until(10_000))





























########################################################################################################
## C. Hanze week 3
########################################################################################################




# opgave 1
### A
class A:
    def __init__(self, i = 0):
        self.i = i
    
    def m1(self):
        self.i += 1

class B(A):
    def __init__(self, j = 0):
        super().__init__(3)
        self.j = j
    
    def m1(self):
        self.i += 1
    
def main():
    b = B()             # b.i = 3  b.j = 0
    print(b.i, b.j)     #  3 0
    b.m1()              # b.i = 4  b.j = 0
    print(b.i, b.j)     #  4 0

main()



### B
class A:
    def __init__(self, i):
        self.i = i
    
    def __str__(self):
        return "I am class A"

class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    
    def __str__(self):
        return "I am class B"


def main():
    a = A(1)            # a.i = 3
    b = B(1, 2)         # b.i = 1   b.j = 2
    print(a)            # "I am class A"
    print(b)            # "I am class B"
    print(a.i)          # 3
    print(b.i, b.j)     # 1 2

main()


# opgave 2
#  NEE



# opgave 3
class Circle():
    PI = 3.14159265358979

    def __init__(self, straal):
        self.straal = straal
    
    def area(self, persision = 2):
        return round(self.straal * self.straal * self.PI, persision)    
    
    def perimeter(self, persision = 2):
        return round(self.straal * 2 * self.PI, persision)


c = Circle(8)
print(c.area())
# assert c.area() == 200.96
# assert c.perimeter() == 50.24
# assert c.perimeter() == 50.24




# opgave 4
class Roman():
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @classmethod
    def roman_to_int_me(self, roman):
        return eval(self.__roman_to_int_inner(roman))

    @classmethod
    def __roman_to_int_inner(self, roman):
        if len(roman) == 1:
            return str(self.rom_val[roman])

        if self.rom_val[roman[-2]] < self.rom_val[roman[-1]]:
            return "{} - {}".format(self.rom_val[roman[-1]], self.__roman_to_int_inner(roman[:-1]))
        else:
            return "{} + {}".format(self.rom_val[roman[-1]], self.__roman_to_int_inner(roman[:-1]))

    @classmethod
    def roman_to_int(cls, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range (len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                print("+=", rom_val[s[i]], - 2 * rom_val[s[i - 1]])
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else: 
                print("+=", rom_val[s[i]])
                int_val += rom_val[s[i]]
        return int_val

# assert Roman.roman_to_int('C') == 100
assert Roman.roman_to_int('XLIX') == 49
# assert Roman.roman_to_int('MMMCMLXXXVI') == 3986


# opgave 5
class Stack:
    def __init__(_):
        _.__elements = []
        _.__index = 0
    
    # Return True if the stack is empty
    def is_empty(_):
        return _.__index == 0
    
    # Return the element at the top of the stack
    # without removing it from the stack.
    def peek(_):
        if self.is_empty():
            return none
        else:
            return _.__elements[_.__index-1]
    
    # Store an element at the top of the stack
    def push(_, value):
        if len(_.__elements) > _.__index:
            _.__elements[_.__index] = value
        else:
            _.__elements.append(value)
        _.__index += 1
        
    # Remove the element at the top of the stack and return it
    def pop(_):
        if self.is_empty():
            return none
        else:
            _.__index -= 1
            return _.__elements[_.__index]
    
    # Return the size of the stack
    def get_size(_):
        return _.__index


stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.is_empty():
    # prints9 8 7 6 5 4 3 2 1 0
    print(stack.pop(), end = " ")


# opgave 6 
import time

class StopWatch():
    def __init__(_):
        _.__start_time = 0
        _.__stop_time = 0
        _.start()

    def start(_):
        _.__start_time = time.time()

    def stop(_):
        _.__stop_time = time.time()

    def get_elapsed_time(_):
        return _.__stop_time - _.__start_time

    def getStartTime(_):
        return _.__start_time

    def getStopTime(_):
        return _.__stop_time


size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")



# opgave 7
# try:
#     statement1
#     statement2
#     statement3      # ALs de regel hierboven een exception gooit van wordt deze regel niet uitgevoert

# except Exception1:
#     # Handle exception

# except Exception2:
#     # Handle exception

# except Exception3:
#     # Handle exception

# finally:
#     statement4

# statement5



# opgave 8
import json, requests, sys
from pprint import pprint

# get command line arguments
# if len(sys.argv) < 2:
#     sys.exit()

# argument 0 is program name
location = ' '.join(sys.argv[1:])

# download JSON data
# api key = 842af58c3d0f07bb8fb62b5199a09350
url='http://api.openweathermap.org/data/2.5/forecast?id={}&APPID=842af58c3d0f07bb8fb62b5199a09350'.format(location)
response = requests.get(url)
response.raise_for_status()

# load JSON data into Python variable
weatherData = json.loads(response.text)

w = weatherData['list']
print(weatherData)
print(w)





# opgave 9
# ik miste alleen een dubbele enter voor de class en op 2 plekken tonden onnodige extra spaties na de code 
# ik ben wel verbaast dat mijn stuckje om self te vervangen met underscore geen problemen oplevert in pep8

import time


class StopWatch():
    def __init__(_):
        _.__start_time = 0
        _.__stop_time = 0
        _.start()

    def start(_):
        _.__start_time = time.time()

    def stop(_):
        _.__stop_time = time.time()

    def get_elapsed_time(_):
        return _.__stop_time - _.__start_time

    def getStartTime(_):
        return _.__start_time

    def getStopTime(_):
        return _.__stop_time


size = 1000000
stopWatch = StopWatch()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stop()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")





























########################################################################################################
## D. Hanze week 4
########################################################################################################

# opgave 1

from tkinter import *
from random import randint
import time

class Plot:
    def __init__(_):
        s = 1
        x2 = 50
        y2 = _.__value_to_y(randint(0,100))
        _.__setup()

    def __value_to_y(val):
        return 550-5*val

    def __setup():
        root = Tk()
        root.title('simple plot')

        canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
        canvas.pack(expand=YES, fill=BOTH)

        Button(root, text='Quit', command=root.quit).pack()

        canvas.create_line(50,550,1150,550, width=2) # x-axis
        canvas.create_line(50,550,50,50, width=2)    # y-axis


    def step():
        global s, x2, y2  # We halen hier de waardes uit de global scope zodat python niet opnieuw 
                        # copie"en van de variabelen in het geheugen rond gaat gooien. 
                        # Deze regel is dus niet verplicht maar wel een goede optimalisatie
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            canvas.delete('temp') # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s*50
        y2 = __value_to_y(randint(0,100))
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s+1
        canvas.after(300, step)

    def start():
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            canvas.create_text(x,550, text='%d'% (10*i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
            canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

        canvas.after(300, step)
        root.mainloop()




# opgave 2

import json
from pprint import pprint

with open('books.json') as f:
    books = json.load(f)


### A
def avg_python_price(books):
    value, count = (0,0)
    for book in books:
        if book["topic"] == "Python":
            value += book["price"]
            count += 1

    return format(value / count, '.2f')

print(avg_python_price(books))


### B
def sorted_result(books):
    return sorted(books, key=lambda x: x["author"].split(" ")[-1:])

pprint(sorted_result(books))




# opgave 3  TODO
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from pprint import pprint
import json

def show_result():
    analyze_file(filename.get())

def analyze_file(filename):
    try:
        with open(filename) as f:
            json_input = json.load(f)

        # your code
        counts = {0 : 3, 1 : 7, 2 : 5}
        i = 3
        for item in json_input:
            counts[i] = item["price"]
            i += 1

        pprint(counts)

        # display a histogram for counts
        show_histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File", "File " + filename + " does not exist") 

def open_file():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)

def show_histogram(counts):
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts.values())

    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts, (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10, text = chr(i + ord('a')))

window = Tk()
window.title("Words Frequency Histogram")

frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width = 500, height = 200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 40, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = open_file).pack(side = LEFT)
Button(frame2, text = "Show Result", command = show_result).pack(side = LEFT)

window.mainloop()



# opgave 5
from collections import namedtuple

Node = namedtuple("Node", "data, left, right")

tree = Node(1,
            Node(2,
                Node(4,
                Node(7, None, None),
                None),
            Node(5, None, None)),
        Node(3,
            Node(6,
                Node(8, None, None),
                Node(9, None, None)),
            None))

def preorder(node):
    print(node.data)
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

preorder(tree)




















########################################################################################################
## E. Proeftoets
########################################################################################################

def hex_char(value):
    """Convert a numeric value to one of the possible hexadecimal values
    
    Remember, possible hexadecimal values are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F.
    This is a base 16 type conversion and as such value cannot be higher than 16:
    
    0 => '0'
    ...
    16 => 'F'
    
    We handle two possible cases, first is the conversion of a value between 0 and 9 to 
    its textual representation ('0' ... '9'), the second case is converting numbers 10 to 16 
    into a textual representation from 'A' to 'F'. All is done by using the value's ASCII
    code number, e.g. the vale of ord('A') will be 65 and chr(65) will convert this back to 'A'.
    """
    if value <= 9 and value >= 0:
        # assert str(4) == chr(4 + ord('0')) == '4'
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# given the above, what exactly happens when value > 9 ?   
for x in range(10, 16):
    v = x - 10 + ord('A') # ord('A') == 65
    print("Value: {} - 10, ASCII number: {}, ASCII value => {}".format(x, v, chr(v)))




"""
We weten nu dat de hex_var functie een getal kleiner of gelijk aan 16 kan omzetten naar een hexadecimale 
waarde. Maar hoe nu elke mogelijke decimale waarde om te zetten naar een hexadecimale representatie? 
Het probleem is dus hoe we elk mogelijk getal kunnen reduceren tot een veelvouden van 16.

Ter vergelijking: werken met het decimale stelsel is heel gewoon voor mensen en we kunnen gemakkelijk een 
getal als 279 opbreken in veelvouden van 10 (** is een machtsverheffing):

279 == 2 * (10**2) + 7 * (10**1) + 9 * (10**0)

Op basis van dit principe moeten we een getal opdelen in veelvouden van 16 (in plaats van 10). In de opgave 
wordt de hint gegeven de modulus % en integer division // te gebruiken, de uitwerking is ook tijdens het 
college CS besproken.
"""




def to_hex(decimal):
    """Convert a any decimal to its hexadecimal representation
    """
    # our final hexadecimal result value
    result = ''
    
    while decimal != 0:
        hex_value = decimal % 16
        result = hex_char(hex_value) + result
        decimal = decimal // 16

    return result

assert to_hex(79) == "{0:X}".format(79)
assert to_hex(279) == "{0:X}".format(279)

to_hex(279) # '117'

"""
De hexadecimale waarde 117 komt overeen met:

279 == 1 * (16**2) + 1 * (16**1) + 7 * (16**0)


"""





"""
Stream


Een uitwerking van oefenopgave 2

Een stream is een (on)eindig aantal signalen dat kan worden gelezen, denk bijvoorbeeld aan een 
bewegingssensor die elke keer dat een beweging wordt gedetecteerd een signaal stuurt. Maar denk ook aan 
de genoom opgave, daar was een signaal een opeenvolgend karakter in een (eindige) string.

Tijdens het werkcollege is het principe van een state machine geïnroduceerd: op een enkel moment kan iets 
zich maar in één bepaalde staat bevinden. Bijvoorbeeld, een lamp kan alleen maar aan of uit zijn en in de 
genoom opgave kon een gen in een genoom worden gevonden als het begon met ATF en eindigde met 
TAG, TAA of TGA.

In deze opgave gebeurt hetzelfde en gaan we werken met het volgende protocol:

de eerste 12 karakters is een mac adres
vervolgens 3 hexadecimale karakters die de lengte van de packet aangeven
verdere karakters tot en met de lengte is de inhoud van de packet

"""

with open('data/streams/packets.txt') as handle:
    packet_stream = handle.read()

packet_stream


"""
Wat zijn in dit geval de state(s) waar we mee moeten gaan werken? Weer hebben we te maken met een 
opeenvolging (iteration) en moeten eerst een mac adres weten om vervolgens een lengte te kunnen kennen, 
om vervolgens tot een bepaalde lengte te blijven lezen om de waarde van het packet te vinden 
(en waarna de cyclus weer opnieuw begint).

De states waar we in geïnteresseerd zijn om packets te kunnen lezen zijn dus:

een mac addres (wel of niet bekend)
een lengte van de packet (wel of niet bekend)
In de uitwerking wordt er van uitgegaan dat we met een continue stroom werken, m.a.w. dat we niet weten 
wat het volgende karakter is. Dit betekent dat we steeds naar achteren moeten kijken, dit in 
tegenstelling tot het de genoom opgave waar we vooruit konden kijken (het volgende karakter was immers 
al bekend omdat we de gehele sequentie al kenden).
"""


packet_list = []  # list for collecting extracted packets

# possible states we need to check:
# mac address, empty string or not empty if set
mac = ''

# the packet length, 0 or > 0 if set
# note: keeping it simple, we assume there are no 0 length packets
length = 0

length_as_hex = None

# collect characters as we go (look behind!), should get reset on any state change
chars = ''

for char in packet_stream:
    chars += char
    if not mac: # reference equality check, in this case (string) also evaluates as: mac == ''
        if len(chars) == 12:
            mac = chars # set mac
            chars = ''  # state change, reset chars
        continue        # check actual mac state in next iteration, continue
    
    # at this point the mac address is known
        
    if length == 0: # value equaltity check, in this case (int) also evaluates as: length is 0
        if len(chars) == 3:
            length = int(chars, 16) # set the packet length (a base 16 string to int conversion)
            length_as_hex = chars # set the hexadecimal length value, we need it later
            chars = '' # state change, reset chars 
        continue  # check actual length state in next iteration, continue
    
    # at this point the packet length is known
        
    if len(chars) == length:
        packet_list.append( (mac, length_as_hex, chars) ) # packet length reached
        
        length = 0  # full state reset
        mac = chars = ''

packet_list












"""
Employees


Een uitwerking van opgave 3

In deze oplossing zie je een aantal handige methoden om de klassen compact en efficiënt (pythonic?) uit te werken:

het gebruik van de property class method decorator om een salaris te berekenen
__repr__ (en __str__) is natuurlijk éénmaal gedefiniëerd, met behulp van:
f-string formatting (sinds python 3.6)
*args voor het verzamelen van positionele argumenten
bonus in de Manager class als een keyword argument met een default waarde
Tijdens het werkcollege is kort type hinting genoemd als een recente ontwikkeling om objecten te kunnen annoteren, je kan een toepassing van deze notatie in de uitwerking zien.

N.B: in de opgave wordt gevraagd __repr__ te implementeren om een object te kunnen printen. Het is meer gangbaar hier __str__ voor te gebruiken omdat __repr__ voornamelijk bedoeld is voor de object representatie (zie einde uitwerking opgave).
"""


from typing import Union

class Employee:
    """A company employee class
    """
    def __init__(self, name: str, role: str, department: str, salary: Union[int, float]):
        self.name = name
        self.role = role
        self.department = department
        self.salary = int(salary) # can't be bothered with cents
    
    @property
    def calculated(self) -> int:
        """Return a calculated salary
        """
        # nothing to compute, just return salary
        return self.salary
    
    def __str__(self) -> str:
        # f-string, since python 3.6
        return f"{self.name}, {self.role} at {self.department}, €{self.calculated/1000:.1f}k"

    def __repr__(self) -> str:
        # hex(id(self)) will return the hexadecimal memory address of this object
        return f"<{self.__class__.__name__}: {self.name} at {hex(id(self))}>"




class Manager(Employee):
    """A company manager class
    """
    def __init__(self, *args, bonus: Union[int, float]=0):
        super().__init__(*args)
        self.bonus = bonus
    
    @property
    def calculated(self) -> int:
        """Return a calculated salary
        
        Adds bonus as a percentage of the employee salary.
        """
        # bonus can be a float or int which matters for the 
        # calculation, but cast final result to int
        return int(self.salary + self.salary * self.bonus / 100)




employees = [
    Employee('Julia', 'Accountmanager', 'Products', 18000.99),
    Manager('Jane', 'VP Sales', 'Sales', 45000, bonus=5),
    Employee('John', 'Aftersales specialist', 'Sales', 21000),
    Manager('Bob', 'Head of R&D', 'Products', 35000.75, bonus=8.0),
    Manager('Mary', 'VP Human Resources (bonus next year!)', 'HRM', 30000)
]

for employee in employees:
    print('=>', employee)



"""
=> Julia, Accountmanager at Products, €18.0k
=> Jane, VP Sales at Sales, €47.2k
=> John, Aftersales specialist at Sales, €21.0k
=> Bob, Head of R&D at Products, €37.8k
=> Mary, VP Human Resources (bonus next year!) at HRM, €30.0k
Om het verschil tussen __str__ en __repr__ duidelijk te maken, zie wat er gebeurt als we het employees list object opvragen:
"""


employees[:2]  # [<Employee: Julia at 0x7f4b742fe128>, <Manager: Jane at 0x7f4b742fef28>]