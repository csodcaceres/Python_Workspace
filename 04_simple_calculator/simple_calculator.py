
"""
simple_calculator.py

This script implements a simple command-line calculator that allows the user to perform basic operations:
addition, subtraction, multiplication, division, and exponentiation. The user is prompted to enter two numbers
and select the desired operation. Custom error messages are shown for invalid operations and division by zero.
"""

# Step 1: Ask the user for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Ask for the operation
print("Select the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponentiation (^)")
op = input("Enter the symbol or number of the operation: ").strip()

# Step 3: Perform the selected operation
result = None
operation = ""
try:
	if op in ("1", "+"):
		result = num1 + num2
		operation = f"{num1} + {num2}"
	elif op in ("2", "-"):
		result = num1 - num2
		operation = f"{num1} - {num2}"
	elif op in ("3", "*"):
		result = num1 * num2
		operation = f"{num1} * {num2}"
	elif op in ("4", "/"):
		if num2 == 0:
			raise ZeroDivisionError
		result = num1 / num2
		operation = f"{num1} / {num2}"
	elif op in ("5", "^"):
		result = num1 ** num2
		operation = f"{num1} ^ {num2}"
	else:
		print("\n[ERROR] Invalid operation. Please choose a correct option.")
		exit(1)
	print("\n---- Calculator Result ----")
	print(f"{operation} = {result}")
	print("--------------------------")
except ZeroDivisionError:
	print("\n[ERROR] Cannot divide by zero.")

