from main import *
import random

def main ():
    alfabeto = definir_alfabeto()
    lenguaje1 = generar_lenguaje(alfabeto, random.randint(3, 10))
    lenguaje2 = generar_lenguaje(alfabeto, random.randint(3,10))  
    lenguaje3 = generar_lenguaje(alfabeto, random.randint(3,10))  

    


# Definir el lenguaje como un conjunto de palabras
def definir_alfabeto():
    n = int(input("¿Cuantos simbolos tendrá el alfabeto? "))
    
    # Inicializar el conjunto del lenguaje
    alfabeto = set()
    
    for i in range(n):
        simbolo = input(f"Ingrese el simbolo {i+1}: ")
        alfabeto.add(simbolo)
    
    return alfabeto

def generar_lenguaje(alfabeto, longitud):
    return set(generar_combinaciones(alfabeto, longitud))

def unir_lenguajes(lenguaje1, lenguaje2):
    union= set()
    for palabra in lenguaje1:
        union.add(palabra)
    for palabra in lenguaje2:
        if palabra not in union:
            union.add(palabra)
    
    return union

def concatenar_lenguajes(lenguaje1,lenguaje2):
    concatenaciones = set()
    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            concatenaciones.add(palabra1 + palabra2)
    return concatenaciones

def calcular_cerradura_estrella(lenguaje1):
    longitud_maxima = 3
    estrella.add('epsilon')
    estrella = set()
    for palabra in lenguaje1:
        for i in range(1, longitud_maxima + 1):
            estrella.add(palabra * i)
    return estrella

def calcular_cerradura_positiva(lenguaje1):
    longitud_maxima = 3
    estrella = set()
    for palabra in lenguaje1:
        for i in range(1, longitud_maxima + 1):
            estrella.add(palabra * i)
    return estrella
    
main()