"""
juego_ahorcado.py

Este programa permite jugar al clásico juego del Ahorcado en la consola.
El sistema elige una palabra secreta al azar de una lista y el jugador debe
adivinarla letra por letra. El jugador tiene 6 vidas; cada letra incorrecta
consume una vida. El juego termina cuando se adivina la palabra o se pierden
todas las vidas.

Funciones principales:
- elegir_palabra(): devuelve una palabra aleatoria.
- mostrar_tablero(): muestra la palabra con guiones y letras adivinadas.
- pedir_letra(): solicita al jugador una letra válida no usada previamente.
- ha_ganado(): verifica si el jugador adivinó todas las letras.
- jugar_ahorcado(): ejecuta el flujo principal del juego.

Requisitos:
- Python 3.x
- Librería random: random.choice()

Autor: Caceres Oscar D.
Version: 1.0
Fecha: 2024-06-18
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

# ----- Funciones -----
def elegir_palabra():
    """Devuelve una palabra secreta aleatoria de la lista."""
    palabras = ["python", "ahorcado", "programa", "computadora",
                "desarrollo", "algoritmo", "variable", "funcion",
                "entero", "cadena", "prueba", "desafio", "cerveza",
                "misterio"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    """Devuelve la palabra mostrando guiones para las letras no adivinadas."""
    tablero = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    return " ".join(tablero)

def pedir_letra(letras_usadas):
    """Solicita al jugador una letra válida y no repetida."""
    while True:
        letra = input("Elige una letra: ").lower().strip()
        if len(letra) != 1:
            print("⚠️ Ingresa solo UNA letra.")
        elif not letra.isalpha():
            print("⚠️ Ingresa solo LETRAS (a-z).")
        elif letra in letras_usadas:
            print("⚠️ Ya elegiste esa letra antes.")
        else:
            return letra

def ha_ganado(palabra, letras_adivinadas):
    """Verifica si el jugador ha adivinado todas las letras de la palabra."""
    return all(letra in letras_adivinadas for letra in palabra)

# ----- Juego principal -----
def jugar_ahorcado():
    """Ejecuta el flujo principal del juego del Ahorcado."""
    print("🎮 Bienvenido al juego del Ahorcado 🎮")
    
    palabra = elegir_palabra()
    letras_adivinadas = set()
    letras_usadas = set()
    vidas = 6

    while vidas > 0:
        # Mostrar estado del tablero, vidas y letras usadas
        print("\nPalabra:", mostrar_tablero(palabra, letras_adivinadas))
        print(f"Vidas restantes: {vidas}")
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Ninguna'}")

        # Pedir letra al jugador
        letra = pedir_letra(letras_usadas)
        letras_usadas.add(letra)

        # Evaluar si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f"✅ ¡Bien! La letra '{letra}' está en la palabra.")
            if ha_ganado(palabra, letras_adivinadas):
                print("\n🎉 ¡Felicidades! Has adivinado la palabra:", palabra)
                break
        else:
            vidas -= 1
            print(f"❌ La letra '{letra}' no está en la palabra.")

    # Mensaje si se pierden todas las vidas
    if vidas == 0:
        print("\n😢 Te quedaste sin vidas. La palabra era:", palabra)

# --------------- Ejecutar ---------------
if __name__ == "__main__":
    jugar_ahorcado()



