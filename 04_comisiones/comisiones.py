"""
comisiones.py
-------------

Este programa calcula la comisión de un vendedor. Solicita al usuario
que ingrese su nombre y el total de sus ventas del mes. Luego, calcula
el 13% de las ventas como comisión y muestra el resultado formateado
en pantalla, indicando el monto que le corresponde al vendedor.

Requisitos:
- Python 3.x

Autor: Caceres Oscar D.
Version: 1.0
Fecha: 2019-06-16
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

# Programa para calcular comisión del 13%

# Pedir datos
nombre = input("¿Cómo te llamás?: ")
ventas = float(input("¿Cuánto vendiste este mes?: "))

# Calcular comisión (13%)
comision = ventas * 0.13

# Mostrar resultado con dos decimales
print(f"{nombre}, tu comisión es de ${comision:.2f}")