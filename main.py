def main():
    print("Se ejecuta")
    #validarCadenaConFunciones(array)
main()

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