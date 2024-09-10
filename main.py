def main():
    print("Se ejecuta")
    lenguaje = definir_lenguaje()
    cadena = input("Ingrese la cadena a verificar: ")
    pertenece_al_lenguaje(lenguaje, cadena)

    # Solicitar al usuario un prefijo y un sufijo
    prefijo = input("Ingrese el prefijo a buscar: ")
    sufijo = input("Ingrese el sufijo a buscar: ")
    buscar_por_prefijo_sufijo(lenguaje, prefijo, sufijo)  


main()


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


# Función para verificar si las palabras del lenguaje contienen el prefijo o sufijo dados
def buscar_por_prefijo_sufijo(lenguaje, prefijo, sufijo):
    palabras_encontradas = [palabra for palabra in lenguaje if palabra.startswith(prefijo) or palabra.endswith(sufijo)]
    
    if palabras_encontradas:
        print(f"Palabras que comienzan con '{prefijo}' o terminan con '{sufijo}':")
        for palabra in palabras_encontradas:
            print(palabra)
    else:
        print(f"No se encontraron palabras que comiencen con '{prefijo}' o terminen con '{sufijo}'.")
