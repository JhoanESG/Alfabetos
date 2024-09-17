import random

def main ():
    res = reemplazar_caracteres("Hooooslaed", 'o', 'i')
    res = invertir_cadena(res)
    res = reemplazar_por_aleatorio(res)
    print(res)

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

main()