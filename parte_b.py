from main import *
import random   
import itertools

def generar_palindromos_desde_caracteres(conjunto_cadenas):
    # Separar cada carácter del conjunto de cadenas en una lista de caracteres
    caracteres = ''.join(conjunto_cadenas)
    
    # Lista para almacenar los palíndromos generados
    palindromos = set()
    max_longitud = 6
    cantidad = 15
    # Generar permutaciones de distintos tamaños
    for longitud in range(2, max_longitud + 1):  # Definir la longitud máxima de los palíndromos
        for perm in itertools.product(caracteres, repeat=longitud):
            perm_str = ''.join(perm)
            
            # Verificar si la combinación es un palíndromo
            if perm_str == perm_str[::-1]:
                palindromos.add(perm_str)
    
    # Convertir el conjunto de palíndromos a una lista
    lista_palindromos = list(palindromos)
    
    # Si hay menos de 15 palíndromos, devolver todos
    if len(lista_palindromos) <= cantidad:
        return lista_palindromos
    
    # Seleccionar aleatoriamente `cantidad` palíndromos
    return random.sample(lista_palindromos, cantidad)

def pertenece_al_alfabeto(cadena, alfabeto):
    # Convertir el conjunto de strings en un conjunto de caracteres
    conjunto_caracteres = set("".join(alfabeto))
    
    # Verificar si todos los caracteres en la cadena están en el conjunto de caracteres
    for caracter in cadena:
        if caracter not in conjunto_caracteres:
            return False
    return True

def es_palindromo(cadena, alfabeto):
    # Primero verificamos si la cadena pertenece al alfabeto
    cadena_limpia = cadena.replace(" ", "").lower()  # Limpiamos la cadena
    if not pertenece_al_alfabeto(cadena_limpia, alfabeto):
        return "La cadena ingresada no pertenece al alfabeto dado."
    
    # Si pertenece al alfabeto, verificar si es un palíndromo
    if cadena_limpia == cadena_limpia[::-1]:
        return "¡SI!, la cadena ingresada es un palíndromo."
    else:
        return "¡NO!, la cadena ingresada no es un palíndromo."

def reemplazar_caracteres(cadena, caracter, reemplazo):
    nueva_cadena = ""
    
    for c in cadena:
        if c == caracter:
            nueva_cadena += reemplazo
        else:
            nueva_cadena += c 

    return nueva_cadena
    
def invertir_cadena(cadena):
    nueva_cadena = ""
    
    # Recorremos la cadena de manera inversa
    for i in range(len(cadena)-1, -1, -1):
        nueva_cadena += cadena[i]
    
    return nueva_cadena

def reemplazar_por_aleatorio(cadena):
    caracter_aleatorio = random.choice(cadena)
    
    nueva_cadena = ""
    for _ in cadena:
        nueva_cadena += caracter_aleatorio
    
    return nueva_cadena

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
    estrella.append('ε')
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