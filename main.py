def main():

    alfabeto= definir_lenguaje()
    longitud_palabra = int(input("¿Cuál es la longitud de las palabras que quieres generar? "))
    combinaciones = generar_combinaciones(alfabeto, longitud_palabra)
    imprimir_combinaciones(combinaciones)
    lenguaje = definir_lenguaje()
    cadena = input("Ingrese la cadena a verificar: ")
    pertenece_al_lenguaje(lenguaje, cadena)
    # Solicitar al usuario un prefijo y un sufijo
    prefijo = input("Ingrese el prefijo a buscar: ")
    sufijo = input("Ingrese el sufijo a buscar: ")
    buscar_por_prefijo_sufijo(lenguaje, prefijo, sufijo)

# Función recursiva para generar todas las combinaciones de longitud dada
def generar_combinaciones(alfabeto, longitud):
    if longitud == 0:
        return ['']
    combinaciones_previas = generar_combinaciones(alfabeto, longitud - 1)
    nuevas_combinaciones = []
    
    for simbolo in alfabeto:
        for combinacion in combinaciones_previas:
            nuevas_combinaciones.append(simbolo + combinacion)
    
    return nuevas_combinaciones

# Definir el lenguaje como un conjunto de palabras
def definir_lenguaje():
    # Preguntar cuántas palabras tendrá el lenguaje
    n = int(input("¿Cuántas palabras tendrá el lenguaje? "))
    
    # Inicializar el conjunto del lenguaje
    lenguaje = set()
    
    # Recolectar las palabras del lenguaje
    for i in range(n):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        lenguaje.add(palabra)
    
    return lenguaje

# Verificar si una cadena pertenece al lenguaje
def pertenece_al_lenguaje(lenguaje, cadena):
    if cadena in lenguaje:
        print(f"La cadena '{cadena}' pertenece al lenguaje.")
    else:
        print(f"La cadena '{cadena}' NO pertenece al lenguaje.")


def imprimir_combinaciones(combinaciones):
     # Mostrar las combinaciones
    print("Todas las posibles palabras generadas son:")
    for combinacion in combinaciones:
        print(combinacion)

def validarCadenaConFunciones(array_caracteres):
    # Solicitar la entrada de la cadena desde la terminal
    cadena = input("Por favor ingrese una cadena: ")

    # Comprobar las tres condiciones
    es_valido_alfabeto = tieneSoloLetrasDelAlfabeto(cadena, array_caracteres)
    tiene_minimo_dos = tieneMinimoDosCaracteres(cadena)
    tiene_secuencia_dos = tieneSecuenciaDosCaracteres(cadena)

    # Verificar si todas las condiciones son True
    if es_valido_alfabeto and tiene_minimo_dos and tiene_secuencia_dos:
        print("La cadena ingresada cumple con todas las condiciones.")
        #return True
    else:
        print("La cadena ingresada no cumple con todas las condiciones.")
        #return False

def tieneSoloLetrasDelAlfabeto(cadena, array_caracteres):
    # Convertimos la lista de caracteres en un conjunto para optimizar las búsquedas
    conjunto_caracteres = set(array_caracteres)
    
    # Recorremos cada letra de la cadena y verificamos si está en el conjunto
    for letra in cadena:
        if letra not in conjunto_caracteres:
            return False
    return True

def tieneMinimoDosCaracteres(cadena):
    return len(cadena) >= 2

def tieneSecuenciaDosCaracteres(cadena):
    # Recorremos la cadena desde el primer hasta el penúltimo carácter
    for i in range(len(cadena) - 1):
        # Comprobamos si el carácter actual es igual al siguiente
        if cadena[i] == cadena[i + 1]:
            return True
    return False

# Función para verificar si las palabras del lenguaje contienen el prefijo o sufijo dados
def buscar_por_prefijo_sufijo(lenguaje, prefijo, sufijo):
    palabras_encontradas = [palabra for palabra in lenguaje if palabra.startswith(prefijo) or palabra.endswith(sufijo)]
    
    if palabras_encontradas:
        print(f"Palabras que comienzan con '{prefijo}' o terminan con '{sufijo}':")
        for palabra in palabras_encontradas:
            print(palabra)
    else:
        print(f"No se encontraron palabras que comiencen con '{prefijo}' o terminen con '{sufijo}'.")

