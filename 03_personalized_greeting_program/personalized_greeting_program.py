"""
personalized_greeting_program.py

This program asks the user for their name, year of birth, and favorite color,
calculates their age, and then displays a personalized greeting using that information.
"""

from datetime import datetime

# Step 1: Ask for the user's details
name = input("Enter your name: ")
year_birth = int(input("Enter your year of birth: "))
color = input("Enter your favorite color: ")

# Step 2: Calculate age
current_year = datetime.now().year
age = current_year - year_birth

# Step 3: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {color} is a beautiful color!")
print("Welcome to the personalized greeting program!")
print("--------------------------------")