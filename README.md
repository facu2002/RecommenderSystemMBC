# Sistema de Recomendación : Modelos basados en el contenido
### Daniel Felipe Gómez Aristizabal
### Facundo José García Gallo
#### Universidad de La Laguna - Gestión del Conocimiento en las Organizaciones


### Índice

1. [Instrucciones de uso](#instrucciones-de-uso)
2. [Explicación de ejecución](#explicación-de-ejecución)
3. [Descripción del código](#Descripción-del-código)
4. [Visualización de documentación](#Visualización-de-documentación)



#### Instrucciones de uso

Antes de explicar cómo ejecutar el script debemos saber qué dependencias necesitamos para poder ejecutarlo. Para ello, debemos instalar la siguiente librería con el comando de python *pip*:

```bash
pip install PyQt5
```

La librería PyQT5 es necesaria para poder ejecutar la interfaz gráfica del script, un sistema sencillo en el que se imprime por pantalla el resultado del sistema de recomendación. 



#### Explicación de ejecución

El resultado de la ejecución del script es el siguiente:

![EjemploEjecucion](EjemploEjecucion.png)

Como podemos apreciar, se divide en dos pequeñas tablas, la primera de ellas muestra toda la información procedente de los cálculos necesarios para realizar la recomendación, como puede ser el valor del DF, el valor del IDF o el valor del TF-IDF, además obviamente de todos los términos relacionados con ese documento (se puede cambiar de documento en las pestañas de la parte superior). La segunda tabla muestra los resultados de la similitud entre documentos, es decir, si nos encontramos en el primer documento, nos muestra la relación de similitud con el resto de documentos, y para ver las demás similitudes, debemos cambiar de documento en las pestañas de la parte superior.



#### Descripción del código

En cuanto a la distribución del código podemos decir que es un código bastante sencillo, ya que no cuenta con una estructura de directorios compleja, todo el código se aloja en la carpeta */src*. Dentro de esta carpeta podemos encontrar el fichero donde se encuentra el programa principal *main.py*, el que debemos ejecutar. Luego nos podemos encontrar con el fichero Recommender.py, donde se encuentra la clase que define el sistema de recomendación y sus métodos. Por último, nos encontramos con el fichero *GUI.py*, donde se encuentra la clase que define la interfaz gráfica del programa.



#### Visualización de documentación


Para la correcta visualización del despliegue de la documentación acceda al link adjunto en el repositorio de GitHub, esto lo llevará directamente a una pestaña del navegador donde puede consultar toda la documentación de nuestro programa.