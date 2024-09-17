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


    
main()