from main import *
import random

def main ():
    alfabeto = definir_alfabeto()
    lenguaje1 = generar_lenguaje(alfabeto, 3)

# Definir el lenguaje como un conjunto de palabras
def definir_alfabeto():
    n = int(input("¿Cuantos simbolos tendrá el alfabeto? \nCantidad: "))
    
    # Inicializar el conjunto del lenguaje
    alfabeto = set()
    print("Ingrese caracteres individuales")
    for i in range(n):
        simbolo = input(f"Ingrese el simbolo {i+1}: ")
        alfabeto.add(simbolo)
    
    return alfabeto

def generar_lenguaje(alfabeto, longitud):
    cantidad = longitud*3
    lista = list(generar_combinaciones(alfabeto, longitud))
    # Si hay menos de 'cantidad' de combinaciones, devolver todos
    if len(lista) <= cantidad:
        return lista
    return random.sample(lista, cantidad)

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
    estrella = []
    estrella.append('epsilon')
    for palabra in lenguaje1:
        for i in range(1, longitud_maxima + 1):
            estrella.append(palabra * i)
    return estrella

def calcular_cerradura_positiva(lenguaje1):
    longitud_maxima = 3
    estrella = []
    for palabra in lenguaje1:
        for i in range(1, longitud_maxima + 1):
            estrella.append(palabra * i)
    return estrella
    
main()