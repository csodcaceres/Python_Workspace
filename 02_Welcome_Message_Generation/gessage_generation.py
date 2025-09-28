"""
generation_message.py
-----------------------

This script generates a personalized welcome message for the user.

Program flow:
1. Asks the user for their name, favorite hobby, and favorite color.
2. Retrieves the current date using the `datetime` library.
3. Displays a dynamic welcome message that includes:
   - The current date
   - The user's name
   - Their favorite hobby
   - Their favorite color

Technical features:
- Uses the standard `datetime` library to handle dates.
- Collects user input through `input()`.
- Formats strings using f-strings for clarity and readability.

Requirements:
- Python 3.x
- Standard library: datetime

Author: Caceres Oscar D.
Version: 1.0
Date: 2019-06-15
License: MIT

Copyright (c) 2020 Caceres Oscar D.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"), 
to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software provided that this copyright 
notice and this license are included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
"""

# Add import for date
import datetime

# Step 1: Ask the user for their name, hobby and favorite color
name = input("What's your name?: ")
hobby = input("What's your favorite hobby?: ")
color = input("What's your favorite color?: ")

# Get current date
current_date = datetime.datetime.now().strftime("%d/%m/%Y")

# Step 2: Generate a personalized welcome message
print(f"\n----------- Welcome Message {current_date} -----------")
print(f"Hello, {name}")
print(f"Welcome to the world of Python programming!")
print(f"It's great to know that you love {hobby}.")
print(f"By the way, {color} is a beautiful color!")
print(f"Get ready to build someting amazing with Python!")
print("--------------------------------------------------\n")
