
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





def main():
    cantidad_simbolos = int(input("¿Cuántos símbolos tendrá el alfabeto? "))






main()