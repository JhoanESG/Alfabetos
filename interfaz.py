import tkinter as tk
from tkinter import messagebox, simpledialog
import parte_b as B
from parte_b import *

def nueva_archivo():
    messagebox.showinfo("Nuevo", "Opción 'Nuevo Archivo' seleccionada")

def abrir_archivo():
    messagebox.showinfo("Abrir", "Opción 'Abrir Archivo' seleccionada")

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
ventana.geometry("400x300")

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
menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Esta es una aplicación de ejemplo"))

boton_reemplazar = tk.Button(ventana, text="Reemplazar Caracter", command=reemplazar_caracter)
boton_reemplazar.pack(pady=20)

boton_invertir = tk.Button(ventana, text="Invertir Cadena", command=invertir_cadena)
boton_invertir.pack(pady=20)

boton_aleatorio = tk.Button(ventana, text="Reemplazar Por Caracter Aleatorio", command=reemplazar_por_aleatorio)
boton_aleatorio.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
