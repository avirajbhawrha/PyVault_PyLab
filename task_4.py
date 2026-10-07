import ast

user_input = input("Enter a value: ")

try:
    value = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    value = user_input

print("Value:", value)

if value:
    print("In Python,", value, "is Truthy")
    print("Python checks whether the value is considered present, non-empty, or non-zero.")
else:
    print("In Python,", value, "is Falsy")
    print("Python checks whether the value is considered empty, zero, absent, or false.")