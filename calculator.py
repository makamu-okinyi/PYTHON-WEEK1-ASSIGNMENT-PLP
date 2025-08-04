# Basic Calculator Program

# Ask for user input
num1 = float(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the selected operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
# End of calculator.py
# This is a simple calculator that performs basic arithmetic operations.