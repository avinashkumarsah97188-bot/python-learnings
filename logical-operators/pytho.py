# Program to demonstrate Relational and Logical Operators

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Relational Operators
print("\nRelational Operators")
print("a == b :", a == b)   # Equal to
print("a != b :", a != b)   # Not equal to
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater than or equal to
print("a <= b :", a <= b)   # Less than or equal to

# Logical Operators
print("\nLogical Operators")
print("(a > 0 and b > 0) :", (a > 0 and b > 0))
print("(a > 0 or b > 0)  :", (a > 0 or b > 0))
print("not(a > b)        :", not(a > b))