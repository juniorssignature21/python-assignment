# 1. How do you declare a variable in Python? Provide an example.
name = 10

# 2. What are the rules for naming variables in Python?
# 1) Donot start a variable name with a number
#  2) use underscore instead of any other special character
# 3) 

# What are the basic data types in Python? Give examples of each.
# Integers
x = 10
# Floating point numbers
y = 10.5
# Strings
z = '10'
# Complex Numbers
m = 3j
# Booleans
x = True
y = False

# 4. How do you convert one data type to another in Python? Provide an example.

name = '20'
print(name)

converted = int(name)
print(converted)
print(type(converted))

# 5. What is type conversion in Python? Why is it necessary?
# Type conversion in Python allows you to transform data from one type to another, ensuring compatibility, validating input, and facilitating operations across different data types.

# 6. Describe the difference between implicit and explicit type conversion in Python.
# 1) implicit
name = str(input("what is your name? "))
age = int(input("How old are you? "))
reply = "My name is " + name + " and i am " + str(age) + " years old"
print(reply)

# Explicit
name_int = 10
name_str = str(name_int)
print(name_str)
print(type(name_str))

# 7. What is the purpose of using comments in Python? Give an example.
# comments are used to explain the purpose of each section of code


# 8. Explain the concept of dynamic typing in Python and its implications for variable declaration and usage.

# Dynamic typing in Python enables variables to change data types dynamically during runtime without the need for explicit type declaration, providing flexibility but requiring careful consideration to avoid unexpected behavior.

# 9. How do you check the data type of a variable in Python?
# You can check the data type of a variable in python by using the built-in 'type()' function
john = 20
print(type(john))

# 10. What are some common built-in functions used for type conversion in Python, and how do you use them?
int()
hell = '90'
hello = int(hell)
print(hell)

float()
hell_one = 90
hello_one = float(hell_one)
print(hello_one)

str()
hell_two = 90
hello_two = str(hell_two)
print(hello_two)

list()
hell_three = (1, 2, 3)
hello_three = list(hell_three)
print(hello_three)

tuple()
hell_four = [1, 2, 3]
hello_four = tuple(hell_four)
print(hello_four)

dict()
hell_five = [("a", 1), ("b", 2), ("c", 3)]
hello_five = dict(hell_five)
print(hello_five)

# 11. Discuss the significance of using meaningful variable names in Python programming. Provide an example.
# using a meaningful variable name makes the programmers code readable and easy to understand

height = '10ft'
# creating a variable for  "height" 
