from main import *


import itertools

def main ():

    #PUNTO 3 FORMAR PALINDROMAS 

    conjunto = {"aba", "xy", "b"}
    palindromos = generar_palindromos_desde_caracteres(conjunto)
    print(f"Palíndromos generados: {palindromos}")

    #PUNTO 4 VERIFICAR QUE ES PALINDROME
    cadena = input("Ingrese la cadena a verificar: ")
    print(es_palindromo(cadena))
    



def generar_palindromos_desde_caracteres(conjunto_cadenas):
    # Unir todas las palabras en un solo string
    todos_los_caracteres = ''.join(conjunto_cadenas)
    
    # Lista para almacenar los palíndromos generados
    palindromos = set()
    
    # Generar todas las permutaciones posibles de los caracteres
    for i in range(2, len(todos_los_caracteres) + 1):  # Tomar combinaciones de diferentes tamaños
        for perm in itertools.permutations(todos_los_caracteres, i):
            perm_str = ''.join(perm)
            
            # Verificar si la combinación es un palíndromo
            if perm_str == perm_str[::-1]:
                palindromos.add(perm_str)
    
    return list(palindromos)


def pertenece_al_alfabeto(cadena, alfabeto):
    # Verificar si todos los caracteres en la cadena están en el alfabeto
    for caracter in cadena:
        if caracter not in alfabeto:
            return False
    return True
def es_palindromo(cadena, alfabeto):
    # Primero verificamos si la cadena pertenece al alfabeto
    cadena_limpia = cadena.replace(" ", "").lower()  # Limpiamos la cadena
    if not pertenece_al_alfabeto(cadena_limpia, alfabeto):
        return "La cadena ingresada no pertenece al alfabeto dado."
    
    # Si pertenece al alfabeto, verificar si es un palíndromo
    if cadena_limpia == cadena_limpia[::-1]:
        return "La cadena ingresada es un palíndromo."
    else:
        return "La cadena ingresada no es un palíndromo."


main()