"""
generador_de_mensaje.py
-----------------------

Descripción:
Script que genera un mensaje de bienvenida personalizado para el usuario. 
Solicita al usuario su nombre, pasatiempo favorito y color favorito, y 
muestra un mensaje dinámico junto con la fecha actual.

Uso:
Ejecutar el script en consola, responder las preguntas y recibir un 
mensaje de bienvenida personalizado.

Requisitos:
- Python 3.x
- Librería estándar: datetime

Autor: Caceres, Oscar D.
Fecha: 2019-09-27
Última modificación: 2025-09-27
Versión: 1.0
Licencia: MIT
"""

# Agregar Liberia para la fecha
import datetime

# Paso 1: Preguntar al usuario por su nombre, pasatiempo y color favorito
name = input("¿Cuál es tu nombre?: ")
hobby = input("¿Cuál es tu pasatiempo favorito?: ")
color = input("¿Cuál es tu color favorito?: ")

# Obtener la fecha actual
fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")

# Step 2: Generar un mensaje de bienvenida personalizado
print(f"\n--------- Mensaje de Bienvenida {fecha_actual} ---------")
print(f"Hola, {name}")
print(f"¡Bienvenido al mundo de la programación en Python!")
print(f"Es genial saber que te gusta {hobby}.")
print(f"Por cierto, ¡{color} es un color hermoso!")
print(f"¡Prepárate para crear algo increíble con Python!")
print("---------------------------------------------------\n")
