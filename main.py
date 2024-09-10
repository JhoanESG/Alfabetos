def main():
    print("Se ejecuta")
    lenguaje = definir_lenguaje()
    cadena = input("Ingrese la cadena a verificar: ")
    pertenece_al_lenguaje(lenguaje, cadena)


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

