# Line starting with '#' are comments. Python ignores them.
# They are useful for explaining code

"""
Python ignores string literals that are not assigned to a variable.
Triple double quotes are used for multi-line comments.
"""

'''
Triple single quotes are used for multi-line comments
'''

# print() function is used to print text to console
print("Hello World")

# The input() function pauses the program and waits for the user to type something.
# It always returns a string.
input("Type an input:")

# Variables are container for storing data
# Type is not required in python. It is inferred.
x = 5
stringData = "Hello World"
booleanData = True
listData = [1,2,3,4,5]
floatData = 5.5

print(x)
print(stringData)
print(booleanData)
print(listData)
print(floatData)

# type() function is used to return a class of the object e.g. <class 'int'>
print(type(floatData))