import tkinter as tk

# Definir una matriz grande (por ejemplo, 100x100)
filas = 100
columnas = 100
matriz_grande = [[0 for _ in range(columnas)] for _ in range(filas)]

# Crear una ventana
ventana = tk.Tk()
ventana.title("Matriz Grande")

# Crear un widget de lienzo (canvas) dentro de la ventana
canvas = tk.Canvas(ventana)
canvas.pack(side="left", fill="both", expand=True)

# Crear una barra de desplazamiento para el eje X
scroll_x = tk.Scrollbar(ventana, orient="horizontal", command=canvas.xview)
scroll_x.pack(side="bottom", fill="x")
canvas.configure(xscrollcommand=scroll_x.set)

# Crear una barra de desplazamiento para el eje Y
scroll_y = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scroll_y.set)

# Función para dibujar la matriz en el lienzo
def dibujar_matriz():
    for i in range(filas):
        for j in range(columnas):
            canvas.create_text(j * 20, i * 20, text=str(matriz_grande[i][j]))

# Llamar a la función para dibujar la matriz
dibujar_matriz()

# Configurar el desplazamiento del lienzo
canvas.config(scrollregion=canvas.bbox("all"))

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
