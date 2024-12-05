# Data Types

# In computer programmming, data types specify the type if data that can be stored inside a variable.
num = 24
# Here, 24(an integer) is assigned to the `num` variable. So the data type of `num` is of the `int` class.

# Since everything is an object in Python programming, data types are actually classes and variables are instances(object) of these classes.

## Numeric Data Types - use to hold numeric values
# Integers(int), floating-point(float) numbers and complex(complex) numbers fall under python numbers category.

# we ca use the `type()` function to know which class a variable or a value belongs to.


# * int - holds signed integers of non-limited length.
num1 = 5
print(num1, 'is of type', type(num1))

# * float - holds floating decimal points and it's accurate up to 15 decimal places.
num2 = 2.0 
print(num2, 'is of type', type(num2))

# * complex - holds complex numbers
num3 = 1+2j
print(num3, 'is of type', type(num3) )

## List Data Type
# List is ordered collection of similar or different types of items separated by commas and enclosed within brackets `[]`. e.g,
languages = ["Swift", "Java", "Python"]

## Access List Items
# To access items from a list, we use the index number (0, 1, 2 ...). e.g

languages = ["Swift", "Java", "Python"]

# access element at index 0
print(languages[0]) # Swift

# access element at index 2
print(languages[2]) # Python

## Tuple Data Type
# Tuple is an ordered sequence of items same as a list.The only differnce is that tuples are immutable.
# Tuples once created cannot be modified
#  We use the parentheses '()' to store items of a tuple.
product = ('Xbox', 499.99)

#  