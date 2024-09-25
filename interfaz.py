import tkinter as tk
from tkinter import messagebox, simpledialog
import parte_b as B
from parte_b import *

alfabeto = set()
lenguaje1 = set()
lenguaje2 = set()
lenguaje3 = set()
palindromos = set()

def nueva_archivo():
    messagebox.showinfo("Nuevo", "Opción 'Nuevo Archivo' seleccionada")

def abrir_archivo():
    messagebox.showinfo("Abrir", "Opción 'Abrir Archivo' seleccionada")

def definir_alfabeto():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global alfabeto

    # Solicitar al usuario la creacion del alfabeto
    alfabeto = B.definir_alfabeto()

    # Mostrar el resultado
    messagebox.showinfo("Alfabeto", alfabeto)

def mostrar_alfabeto():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global alfabeto
    
    # Verificar si el conjunto de palindromos tiene elementos
    if not alfabeto:
        messagebox.showerror("Error", "No ha definido un alfabeto")
        return
    
    messagebox.showinfo("Lenguaje", alfabeto)

def generar_lenguaje():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    #Verificar que exista un alfabeto
    global alfabeto
    if not alfabeto:  # Verifica si alfabeto está vacío
        messagebox.showerror("Error", "Primero debe crear un alfabeto")
        return

    # Pedir datos al usuario
    longitud = simpledialog.askinteger("Entrada", "Ingrese la longitud de las palabras del lenguaje")
    if longitud <= 1:
        messagebox.showerror("Error", "La longitud no es valida")
        return

    global lenguaje1
    global lenguaje2
    global lenguaje3

    # Generar y almacenar el lenguaje
    if not lenguaje1:
        lenguaje = B.generar_lenguaje(alfabeto, longitud)
        lenguaje1 = set(lenguaje)
    elif not lenguaje2:
        lenguaje = B.generar_lenguaje(alfabeto, longitud)
        lenguaje2 = set(lenguaje)
    elif not lenguaje3:
        lenguaje = B.generar_lenguaje(alfabeto, longitud)
        lenguaje3 = set(lenguaje)
    else:
        messagebox.showerror("Error", "Ya tiene 3 lenguajes creados, no puede crear otro")
        return

    # Mostrar el resultado
    messagebox.showinfo("Lenguaje Generado", lenguaje)

def unir_lenguajes():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global lenguaje1
    global lenguaje2
    global lenguaje3

    # Verificar que los 3 lenguajes tengan contenido
    if not lenguaje1 or not lenguaje2 or not lenguaje3:
        messagebox.showerror("Error", "Debe crear 3 lenguajes antes de cualquier operacion")
        return
    
    # Ingresar los lenguajes que se quieren unir
    numLenguajeA = simpledialog.askstring("Entrada", "Ingrese el primer lenguaje para la operacion (numero del lenguaje)")
    if numLenguajeA is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeA:
        case "1":
            a = lenguaje1
        case "2":
            a = lenguaje2
        case "3":
            a = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    # Ingresar los lenguajes que se quieren unir
    numLenguajeB = simpledialog.askstring("Entrada", "Ingrese el segundo lenguaje para la operacion (numero del lenguaje)")
    if numLenguajeB is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeB:
        case "1":
            b = lenguaje1
        case "2":
            b = lenguaje2
        case "3":
            b = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    union = B.unir_lenguajes(a, b)
    messagebox.showinfo("Concatenacion Lenguajes", union)

def concatenar_lenguajes():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global lenguaje1
    global lenguaje2
    global lenguaje3

    # Verificar que los 3 lenguajes tengan contenido
    if not lenguaje1 or not lenguaje2 or not lenguaje3:
        messagebox.showerror("Error", "Debe crear 3 lenguajes antes de cualquier operacion")
        return
    
    # Ingresar los lenguajes que se quieren unir
    numLenguajeA = simpledialog.askstring("Entrada", "Ingrese el primer lenguaje para la operacion (numero del lenguaje)")
    if numLenguajeA is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeA:
        case "1":
            a = lenguaje1
        case "2":
            a = lenguaje2
        case "3":
            a = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    # Ingresar los lenguajes que se quieren unir
    numLenguajeB = simpledialog.askstring("Entrada", "Ingrese el segundo lenguaje para la operacion (numero del lenguaje)")
    if numLenguajeB is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeB:
        case "1":
            b = lenguaje1
        case "2":
            b = lenguaje2
        case "3":
            b = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    union = B.concatenar_lenguajes(a, b)
    messagebox.showinfo("Concatenacion Lenguajes", union)

def calcular_cerradura_estrella():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global lenguaje1
    global lenguaje2
    global lenguaje3

    # Verificar que los 3 lenguajes tengan contenido
    if not lenguaje1 or not lenguaje2 or not lenguaje3:
        messagebox.showerror("Error", "Debe crear 3 lenguajes antes de cualquier operacion")
        return
    
    # Ingresar los lenguajes que se quieren unir
    numLenguajeA = simpledialog.askstring("Entrada", "Ingrese el lenguaje para el que desea la cerradura estrella (numero del lenguaje)")
    if numLenguajeA is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeA:
        case "1":
            a = lenguaje1
        case "2":
            a = lenguaje2
        case "3":
            a = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    estrella = B.calcular_cerradura_estrella(a)
    messagebox.showinfo("Cerradura De Estrella", estrella)

def calcular_cerradura_positiva():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global lenguaje1
    global lenguaje2
    global lenguaje3

    # Verificar que los 3 lenguajes tengan contenido
    if not lenguaje1 or not lenguaje2 or not lenguaje3:
        messagebox.showerror("Error", "Debe crear 3 lenguajes antes de cualquier operacion")
        return
    
    # Ingresar los lenguajes que se quieren unir
    numLenguajeA = simpledialog.askstring("Entrada", "Ingrese el lenguaje para el que desea la cerradura positiva (numero del lenguaje)")
    if numLenguajeA is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeA:
        case "1":
            a = lenguaje1
        case "2":
            a = lenguaje2
        case "3":
            a = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
        
    positiva = B.calcular_cerradura_positiva(a)
    messagebox.showinfo("Cerradura Positiva", positiva)

def mostrar_lenguaje():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global lenguaje1
    global lenguaje2
    global lenguaje3
    
    # Ingresar el lenguaje que se quiere mostrar
    numLenguajeA = simpledialog.askstring("Entrada", "Ingrese el lenguaje que desea observar")
    if numLenguajeA is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    match numLenguajeA:
        case "1":
            if not lenguaje1:
                messagebox.showerror("Error", "El lenguaje 1 no se ha creado")
                return
            a = lenguaje1
        case "2":
            if not lenguaje2:
                messagebox.showerror("Error", "El lenguaje 2 no se ha creado")
                return
            a = lenguaje2
        case "3":
            if not lenguaje3:
                messagebox.showerror("Error", "El lenguaje 3 no se ha creado")
                return
            a = lenguaje3
        case _:
            messagebox.showerror("Error", "El valor ingresado no corresponde con un lenguaje")
            return
    
    messagebox.showinfo("Lenguaje", a)

def generar_palindromos_alfabeto():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    #Verificar que exista un alfabeto
    global alfabeto
    if not alfabeto:  # Verifica si alfabeto está vacío
        messagebox.showerror("Error", "Primero debe crear un alfabeto")
        return

    global palindromos

    # Calcular palindromos con el alfabeto
    palindromos = B.generar_palindromos_desde_caracteres(alfabeto)
    messagebox.showinfo("Palindromos", palindromos)

def es_palindromo():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    #Verificar que exista un alfabeto
    global alfabeto
    if not alfabeto:  # Verifica si alfabeto está vacío
        messagebox.showerror("Error", "Primero debe crear un alfabeto")
        return

    # Ingresar la cadena que se quiere comprobar como palindromo
    cadena = simpledialog.askstring("Entrada", "Ingrese el lenguaje que desea observar")
    if cadena is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return

    # Determinar si es palindromo con el alfabeto
    resultado = B.es_palindromo(cadena, alfabeto)
    messagebox.showinfo("¿Es Palindromo?", resultado)

def mostrar_palindromos():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    global palindromos
    
    # Verificar si el conjunto de palindromos tiene elementos
    if not palindromos:
        messagebox.showerror("Error", "Primero debe generar los palindromos antes de poder verlos")
        return
    
    messagebox.showinfo("Lenguaje", palindromos)

def reemplazar_caracter():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    # Pedir datos al usuario
    cadena = simpledialog.askstring("Entrada", "Introduce la cadena:")
    if cadena is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    caracter = simpledialog.askstring("Entrada", "Introduce el carácter a reemplazar:")
    if caracter is None or len(caracter) != 1:
        messagebox.showerror("Error", "Debes introducir un único carácter")
        return
    
    reemplazo = simpledialog.askstring("Entrada", "Introduce el carácter de reemplazo:")
    if reemplazo is None or len(reemplazo) != 1:
        messagebox.showerror("Error", "Debes introducir un único carácter")
        return

    # Reemplazar el carácter en la cadena
    resultado = B.reemplazar_caracteres(cadena, caracter, reemplazo)
    
    # Mostrar el resultado
    messagebox.showinfo("Resultado", resultado)

def invertir_cadena():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    # Pedir cadena al usuario
    cadena = simpledialog.askstring("Entrada", "Introduce la cadena:")
    if cadena is None:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    # Invertir la cadena
    resultado = B.invertir_cadena(cadena)
    
    # Mostrar el resultado
    messagebox.showinfo("Resultado", resultado)

def reemplazar_por_aleatorio():
    # Crear una ventana oculta para usar simpledialog
    ventana_oculta = tk.Tk()
    ventana_oculta.withdraw()  # Oculta la ventana principal

    # Pedir cadena al usuario
    cadena = simpledialog.askstring("Entrada", "Introduce la cadena:")
    if cadena is None or len(cadena) == 0:
        messagebox.showerror("Error", "No se introdujo ninguna cadena")
        return
    
    # Reemplazar todos los caracteres de la cadena por un carácter aleatorio
    resultado = B.reemplazar_por_aleatorio(cadena)
    
    # Mostrar el resultado
    messagebox.showinfo("Resultado", resultado)

def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Menú en Tkinter")
ventana.geometry("400x650")

# Crear barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Añadir opciones al menú "Archivo"
menu_archivo.add_command(label="Nuevo", command=nueva_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()  # Añade una línea de separación
menu_archivo.add_command(label="Salir", command=salir)

# Crear menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Añadir opciones al menú "Ayuda"
menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Esta es una aplicación para realizar operaciones sobre alfabetos, lenguajes y palabras"))

boton_def_alfabeto = tk.Button(ventana, text="Definir Alfabeto", command=definir_alfabeto)
boton_def_alfabeto.pack(pady=10)

boton_ver_alfabeto = tk.Button(ventana, text="Ver Alfabeto", command=mostrar_alfabeto)
boton_ver_alfabeto.pack(pady=10)

boton_gen_lenguaje = tk.Button(ventana, text="Generar Lenguaje", command=generar_lenguaje)
boton_gen_lenguaje.pack(pady=10)

boton_ver_lenguaje = tk.Button(ventana, text="Ver Lenguaje", command=mostrar_lenguaje)
boton_ver_lenguaje.pack(pady=10)

boton_unir_lenguaje = tk.Button(ventana, text="Unir Lenguajes", command=unir_lenguajes)
boton_unir_lenguaje.pack(pady=10)

boton_conc_lenguaje = tk.Button(ventana, text="Concatenar Lenguajes", command=concatenar_lenguajes)
boton_conc_lenguaje.pack(pady=10)

boton_estrella = tk.Button(ventana, text="Calcular Cerradura De Estrella", command=calcular_cerradura_estrella)
boton_estrella.pack(pady=10)

boton_positiva = tk.Button(ventana, text="Calcular Cerradura Positiva", command=calcular_cerradura_positiva)
boton_positiva.pack(pady=10)

boton_reemplazar = tk.Button(ventana, text="Reemplazar Caracter", command=reemplazar_caracter)
boton_reemplazar.pack(pady=10)

boton_invertir = tk.Button(ventana, text="Invertir Cadena", command=invertir_cadena)
boton_invertir.pack(pady=10)

boton_aleatorio = tk.Button(ventana, text="Reemplazar Por Caracter Aleatorio", command=reemplazar_por_aleatorio)
boton_aleatorio.pack(pady=10)

boton_gen_palindromos = tk.Button(ventana, text="Generar Palindromos", command=generar_palindromos_alfabeto)
boton_gen_palindromos.pack(pady=10)

boton_es_palindromo = tk.Button(ventana, text="Determinar Si Es Palindromo", command=es_palindromo)
boton_es_palindromo.pack(pady=10)

boton_ver_palindromos = tk.Button(ventana, text="Ver Palindromos", command=mostrar_palindromos)
boton_ver_palindromos.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
