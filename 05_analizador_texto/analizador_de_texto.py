"""
analizador_de_texto.py
----------------------

1 - Entrada:

    - Solicite al usuario un texto cualquiera (frase, párrafo, poema, etc.).
    - Solicite al usuario tres letras.

2 - Procesamiento y análisis del texto:

    - Contar letras: Indicar cuántas veces aparece cada letra elegida (ignorando mayúsculas/minúsculas).
    - Contar palabras: Informar cuántas palabras hay en el texto.
    - Primera y última letra: Mostrar la primera y la última letra del texto.
    - Invertir palabras: Mostrar el texto con las palabras en orden invertido.
    - Buscar “Python”: Indicar si la palabra “Python” aparece en el texto.

3 - Sugerencias técnicas:

    - Convertir texto y letras a minúsculas para contar correctamente.
    - Usar métodos de string como .count(), .split(), indexación y .join().
    - Para la búsqueda de “Python” se puede usar un booleano y un diccionario para el mensaje.

Requisitos:
- Python 3.x

Autor: Caceres Oscar D.
Version: 1.0
Fecha: 2019-06-17
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

texto = input('Ingresa un texto a eleccion: ').lower()
letras = [
    input('Ingrese la primera letra: ').lower(),
    input('Ingrese la segunda letra: ').lower(),
    input('Ingrese la tercera letra: ').lower()
]

"""
letras.append(input('Ingresa la primera letra: ').lower())
letras.append(input('Ingresa la segunda letra: ').lower())
letras.append(input('Ingresa la tercera letra: ').lower())
"""

print('\n')
print('CANTIDAD DE LETRAS')

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f'Hemos encontrado la letra {letras[0]} repitidas {cantidad_letras1} veces')
print(f'Hemos encontrado la letra {letras[1]} repitidas {cantidad_letras2} veces')
print(f'Hemos encontrado la letra {letras[2]} repitidas {cantidad_letras3} veces')

print('\n')
print('CANTIDAD DE PALABRAS')
palabras = texto.split()

print(f'Hemos encontrados {len(palabras)} en tu texto')

print('\n')
print('LETRAS DE INICIO Y LETRA FIN')
letras_inicio = texto[0]
letras_fin = texto[-1]
print(f'La letra inicial es {letras_inicio} y la letra final es {letras_fin}')

print('\n')
print('TEXTO INVERTIDO')
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si ordenamos un texto al reves va a decir: {texto_invertido}')

print('\n')
print('BUSCANDO LA PALABRA PYTHON')
buscar_python = 'python' in texto
dic = {True:'si', False:'no'}
print(f'La palabra python {dic[buscar_python]} se encuentra en el texto')

"""
a_buscar = input('Ingrese una palabra a buscar: ').lower()
dic = {True:'si', False:'no'}
print(f"La palabra {a_buscar} {dic[a_buscar in texto]} se encuentra en el texto ingresado")

"""