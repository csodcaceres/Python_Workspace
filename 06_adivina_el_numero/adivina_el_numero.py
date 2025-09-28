
"""
divina_el_numero.py
----------------------

1 - Inicio:
    - El programa pide el nombre del usuario.
    - Explica que ha pensado un número entre 1 y 100 y que el usuario tiene 8 intentos para adivinarlo.

2 - Dinámica del juego:

    - El usuario ingresa un número en cada intento.
    - El programa responde según el número ingresado:
        - Si está fuera del rango (menor a 1 o mayor a 100), indica que no es permitido.
        - Si es menor al número secreto, indica que es incorrecto y menor.
        - Si es mayor al número secreto, indica que es incorrecto y mayor.
        - Si acierta, informa que ganó y cuántos intentos usó.

3 - Repetición:
    - Se repite hasta que el usuario acierte o se agoten los 8 intentos.

4 - Objetivo:
    - Aceptar el desafío, practicar control de flujo, loops y operadores, y disfrutar programando el juego.

Requisitos:
- Python 3.x
- Librería estándar: random

Autor: Caceres Oscar D.
Version: 1.0
Fecha: 2024-06-17
Última modificación: 2025-09-27
Licencia: MIT
Copyright (c) 2024 Caceres Oscar D.

Se concede permiso, sin cargo, a cualquier persona que obtenga una copia 
de este software y archivos de documentación asociados (el "Software"), 
a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar 
y/o vender copias del Software, sujeto a la condición de que se incluya 
este aviso de copyright y esta licencia en todas las copias o partes 
sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO.
"""
import random

def juego_adivinanza():
    # Pedir el nombre del jugador; si no ingresa nada, se asigna "Jugador"
    nombre = input("¿Cómo te llamás?: ").strip() or "Jugador"

    # Generar un número secreto aleatorio entre 1 y 100
    secreto = random.randint(1, 100)

    # Informar al jugador las reglas del juego
    print(f"\nBueno, {nombre}, he pensado un número entre 1 y 100.")
    print("Tenés solo ocho intentos para adivinar cuál es.\n")

    # Definir la cantidad máxima de intentos y contador de intentos actuales
    intentos_max = 8
    intentos = 0

    # Bucle principal del juego: se repite mientras haya intentos disponibles
    while intentos < intentos_max:
        # Pedir al jugador que ingrese un número y limpiar espacios en blanco
        entrada = input(f"Intento {intentos + 1}/{intentos_max} - Elegí un número: ").strip()

        # Validar que la entrada sea un número válido
        if not entrada.isdigit():
            print("⚠️ Eso no es un número válido. Intentalo de nuevo.\n")
            continue
        
        # Convertir la entrada a entero
        num = int(entrada)

        # Validar que el número esté dentro del rango permitido (1-100)
        if num < 1 or num > 100:
            print("⚠️ El número debe estar entre 1 y 100. Intentalo de nuevo.\n")
            continue

        # Contar este intento como válido
        intentos += 1

        # Comparar el número ingresado con el número secreto y dar feedback
        if num < secreto:
            print("Incorrecto: tu número es menor que el número secreto.\n")
        elif num > secreto:
            print("Incorrecto: tu número es mayor que el número secreto.\n")
        else:
            print(f"🎉 ¡Felicidades, {nombre}! Adivinaste el número en {intentos} intento(s).")
            break
    else:
        print(f"❌ Se te acabaron los intentos. El número secreto era {secreto}.")

if __name__ == "__main__":
    juego_adivinanza()
