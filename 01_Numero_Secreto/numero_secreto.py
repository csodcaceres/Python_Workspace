"""
numero_secreto.py
-----------------

Descripción:
Juego simple donde el jugador debe adivinar un número secreto entre 1 y 10. 
El jugador cuenta con 3 intentos para adivinar correctamente. Después de 
cada intento, el juego indica si el número ingresado es demasiado alto, 
demasiado bajo o correcto. Si el jugador falla en todos los intentos, 
el programa revela el número secreto.

Uso:
Ejecutar el script en consola y seguir las instrucciones para ingresar un número.

Requisitos:
- Python 3.x
- Librería estándar: random

Autor: Caceres Oscar D.
Version: 1.0
Fecha: 2019-06-15
Última modificación: 2025-09-27
Licencia: MIT

Copyright (c) 2020 Caceres Oscar D.

Se concede permiso, sin cargo, a cualquier persona que obtenga una copia 
de este software y archivos de documentación asociados (el "Software"), 
a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar 
y/o vender copias del Software, sujeto a la condición de que se incluya 
este aviso de copyright y esta licencia en todas las copias o partes 
sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO.
"""
# -------------------------------------------------------
#                       Libreria
# -------------------------------------------------------
import random

# Se genera un número secreto al azar entre 1 y 10
secret_number = random.randint(1, 10)

# Número máximo de intentos permitidos
attempts = 3

print("Estoy pensando en un número entre 1 o 10")

# Mientras aún queden intentos
while attempts > 0:
    # El jugador ingresa un número
    guess = int(input("Adivina: " ))

    # Si el jugador adivinó correctamente
    if guess == secret_number:
        print("¡Felicidades!, adivinaste el número.")
        break
    # Si el número ingresado es menor al secreto
    elif guess < secret_number:
        print("Demasiado bajo, inténtalo de nuevo.")
    # Si el número ingresado es mayor al secreto
    else:
        print("Demasiado alto, inténtalo de nuevo.")
    
    attempts -= 1

# Si se agotaron los intentos
if attempts == 0:
    print("Lo siento, se te acabaron los intentos. El número secreto era: ", secret_number)

  


