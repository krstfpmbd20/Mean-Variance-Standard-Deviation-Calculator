###############################################
# DATA STRUCTURES
###############################################
# - Introduction to Data Structures and Quick Overview
# - Numbers: int, float, complex
# - Strings: str
# - Boolean (TRUE-FALSE): bool
# - List
# - Dictionary
# - Tuple
# - Set


###############################################
# Introduction to Data Structures and Quick Overview
##############################################

# Numbers: integer
x = 46
type(x)

# Numbers: float
x = 10.3
type(x)

# Numbers: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# List
x = ["btc", "eth", "xrp"]
type(x)

# Dictionary
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Note: List, tuple, set, and dictionary data structures are also referred to as Python Collections (Arrays)

###############################################
# Numbers: int, float, complex
###############################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

#######################
# Changing Types
#######################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Strings
###############################################

print("John")
print('John')

"John"
name = "John"
name = 'John'

#######################
# Multiple Lines Strings
#######################

"""Data Structures: Quick Overview,
Numbers: int, float, complex,
Strings: str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

long_str = """Data Structures: Quick Overview,
Numbers: int, float, complex,
Strings: str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

#######################
# Accessing Elements of Strings
#######################

name
name[0]
name[3]
name[2]

#######################
# Slicing Operation in Strings
#######################

name[0:2]
long_str[0:10]

#######################
# Querying Characters in a String
#######################

long_str

"veri" in long_str

"Veri" in long_str

"bool" in long_str

###############################################
# String Methods 
###############################################

dir(str)

#######################
# len
#######################

name = "john"
type(name)
type(len)

len(name)
len("vahitkeskin")
len("miuul")

#######################
# upper() & lower(): small-major conversions
#######################

"miuul".upper()
"MIUUL".lower()

# type(upper)
# type(upper())


#######################
# replace: changes character
#######################

hi = "Hello AI Era"
hi.replace("l", "p")

#######################
# split: divides
#######################

"Hello AI Era".split()

#######################
# strip: trims
#######################

" ofofo ".strip()
"ofofo".strip("o")


#######################
# capitalize: capitalizes the first letter
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")

###############################################
# List
###############################################

# - Can be changed
# - It is sequential. Index operations can be performed.
# - It is inclusive.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]


###############################################
# List Methods
###############################################

dir(notes)

#######################
# len: built-in python function, size information.
#######################

len(notes)
len(not_nam)

#######################
# append: adds element
#######################

notes
notes.append(100)

#######################
# pop: deletes by index
#######################

notes.pop(0)

#######################
# insert: adds to index
#######################

notes.insert(2, 99)


###############################################
# Dictonary
###############################################

# Can be changed.
# Out of order. (Sorted after 3.7.)
# Inclusive.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"][1]

#######################
# Querying Key
#######################

"YSA" in dictionary

#######################
# Accessing Value by Key
#######################

dictionary["REG"]
dictionary.get("REG")

#######################
# Changing Value
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Accessing All Keys
#######################
dictionary.keys()

#######################
# Accessing All Values
#######################

dictionary.values()


#######################
# Converting All Pairs into a List as a Tuple
#######################

dictionary.items()

#######################
# Updating Key-Value
#######################

dictionary.update({"REG": 11})

#######################
# Adding a New Key-Value
#######################

dictionary.update({"RF": 10})

###############################################
# Tuple
###############################################

# - Cannot be changed.
# - It is sequential.
# - It is inclusive.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)



###############################################
# Set
###############################################

# - Can be changed.
# - Unordered + Unique.
# - It is inclusive.

#######################
# difference(): Difference of two sets
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# Those that are in set1 but not in set2.
set1.difference(set2)
set1 - set2

# Those that are in set2 but not in set1.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): Those who are not relative to each other in both sets
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): Intersection of two sets
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#######################
# union(): Union of two sets
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): Is the intersection of two sets empty?
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# isdisjoint(): Is one set a subset of another set?
#######################

set1.issubset(set2)
set2.issubset(set1)

#######################
# issuperset(): Does one set include another set?
#######################

set2.issuperset(set1)
set1.issuperset(set2)








