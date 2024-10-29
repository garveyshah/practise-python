# Python Variables
# A variable is a container (storage area) to hold data.
number = 10

# Assigning values to Variables
# # assign value to site_name variable
site_name = 'programiz.pro'

print(site_name)

# # Python is an `type-inferred` language, so you don't have to explicitly define the variable type.

# Changing the Value of a Variable 
# # Assigning a new value to site_name
site_name = 'apple.com'

print(site_name)

# # Assigning multiple values to multiplw variables
a, b, c = 5, 3.2, 'Hello'

print (a)
print (b)
print (c)

# If we want to assign the same value to multiple variables at once, we can do this as:
site1 = site2 = 'programiz.com'

print (site1)
print (site2)

## Python Literals 
# Literals are represtations of fixed values in a program.
# They can be numbers, characters, or strings, e.t.c For example, 'Hello, World!', '23.0', 'C', etc.

# Literals are often used to assign values to variables or constants.
site_name = 'Programiz.com'

# In the above expression, 'site_name' is a variable, and 'Programiz.com' is a literal.

## Numerical Literals
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types:
# 'Integer', 'Float', and 'Complex'

##  1. Integer Literals
# Integer literals are numbers without decimal parts. It also consits of negative numbers. e.g '5', '-11', '0', '12' 
#
##  2. Floating-Point Literals
# Floating-point literals are numbers that contain decimal parts.
# Just like integers, floating-point numbers can also be both positive and negative. e.g '2.4', '6.76', '0.0', '-9.45', e.t.c

##  3. Complex Literals
#  Complex literals are numbers that represent complex numbers.
# Here, numerals are in the form 'a + bj', where 'a' is real and 'b' is imaginary. e.g '6+9j',  '2+3j'.

## String Literals
# Texts wrapped inside quotation marks are called string literals
str1 = "This is a string."

# We can alsi use single quotes to create strings.
str2 = 'This is also a string.'

## Boolean Literals
# There are two boolean literals: 'True' and 'False'.
is_pass = True
print(is_pass)

## Character Literals
# Character literals are unicode characters enclosed in a quote.
some_character = 'S'

## Special Literal 
# Python contains one special literal 'None'. We use it to specify a null variable.
value = None

print(value)

## Collection Literals
# Examples are List, Tuple, Dict, and Set literals

# List literal 
fruits = ["apple", "mango", "orange"]
print(fruits)

# tuple literal
numbers = (1, 2, 3)
print(numbers)

# dictionary literal 
alphabets = {'a' :'apple', 'b':'ball', 'c':'cat'}
print(alphabets)

# Set literal
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)


