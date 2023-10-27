import matplotlib.pyplot as plt

# Datos para la tabla
datos = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Crear una figura y ejes
fig, ax = plt.subplots()

# Crear la tabla
tabla = ax.table(cellText=datos, loc='center')

# Ocultar los ejes
ax.axis('off')

# Mostrar la tabla
plt.show()
