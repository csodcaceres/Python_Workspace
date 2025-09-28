"""
file: number_guessing_game.py
-----------------------------

A simple game where the player has to guess a secret number
between 1 and 10. The player has 3 attempts to guess the number.
After each attempt, the game indicates whether the entered number is
too high, too low, or correct.
If the player guesses correctly, they win the game. 
If the number is exhausted, the game ends and the secret number is revealed.

Requirements:
- Python 3.x
- Library: random

Author: Caceres Oscar D.
Version: 1.0
Date: 2019-05-23
License: MIT

Copyright (c) 2024 Caceres Oscar D.

Se concede permiso, sin cargo, a cualquier persona que obtenga una copia 
de este software y archivos de documentación asociados (el "Software"), 
a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar 
y/o vender copias del Software, sujeto a la condición de que se incluya 
este aviso de copyright y esta licencia en todas las copias o partes 
sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO.
"""

# -------------------------------------------------------
#                       Librarys
# -------------------------------------------------------
import random

# A secret number is generated randomly between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of attempts allowed
attempts = 3

print("I'm thinking of a number between 1 or 10")

# While there are still attempts
while attempts > 0:
    # The player enters a number
    guess = int(input("Guess: " ))

    # If the player guessed correctly
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    # If the number entered is less than the secret
    elif guess < secret_number:
        print("Too low, try again.")
    # If the number entered is greater than the secret
    else:
        print("Too high, try again.")
    
    attempts -= 1

# If attempts are exhausted
if attempts == 0:
    print("Sorry, you've run out of attempts. The secret number was:  ", secret_number)

  


