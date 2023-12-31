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

Para la ejecución del script hay que tener en cuenta qué parámetros debemos pasarle. Primero debemos tener un fichero del que se extrae la información de los documentos, este fichero se debe pasar al programa como un parámetro POSIX, este parámetro decidimos nombrarlo como *-f*. Por otro lado debemos tener en cuenta el idioma de ese fichero, ya que en base a eso, determinamos cuáles son las stop-words y el corpus para poder lematizar los documentos. Es por esto que hay que pasarle al programa otro parámetro POSIX con el idioma del documento, este parámetros decidimos nombrarlo como *-l*. Por último podemos determinar cómo será la salida de nuestro programa, si queremos que sea una salida gráfica o una salida por terminal. Para ello creamos un último parámetro POSIX llamado *-p*, este parámetro puede tomar los valores "yes" o "no", en caso de introducir "yes" estamos diciendo que queremos la salida por una interfaz gráfica (en la que utilizamos la librería PyQt5), sin embargo, si introducimos "no" estamos dando a entender que queremos la salida por la terminal.

Por tanto para poder ejecutar el programa debemos poner algo como lo siguiente:

'''bash
python main.py -f ["filename"] -l ["es" | "en"] -p ["yes" | "no"]
'''

Hay que tener en cuenta que el fichero de documentos debe encontrarse en el directorio */data/documents* y cuando pasamos este fichero además de su extensión al programa.


#### Explicación de ejecución

El resultado de la ejecución del script es el siguiente:

![EjemploEjecucion](./images/EjemploEjecucion.png)

Como podemos apreciar, se divide en dos pequeñas tablas, la primera de ellas muestra toda la información procedente de los cálculos necesarios para realizar la recomendación, como puede ser el valor del DF, el valor del IDF o el valor del TF-IDF, además obviamente de todos los términos relacionados con ese documento (se puede cambiar de documento en las pestañas de la parte superior). La segunda tabla muestra los resultados de la similitud entre documentos, es decir, si nos encontramos en el primer documento, nos muestra la relación de similitud con el resto de documentos, y para ver las demás similitudes, debemos cambiar de documento en las pestañas de la parte superior. Hay que tener en cuenta que si el documento es suficientemente grande, al intentar cargar los datos gráficamente puede tardar un poco, por lo que hay que tener paciencia. Incluso cuando la ventana ponga "no responde", tarda un rato en graficarlo.

Sin embargo, si decidimos volcar la información de la salida por la terminal, nos da el mismo resultado pero con diferente interfaz. Primero aparecen todas las frecuencias de los diferentes términos en cada uno de los documentos. Luego aparecen los valores del DF, que son comunes a todos los documentos. A continuación aparece el valor del DF referente a cada documento. Luego aparecen los valores del IDF, que son comunes a todos los documentos, y el valor del tamaño de vector que también es común a todos los documentos. Por último aparecen los valores del TF-IDF referentes a cada documento y los valores de la similitud de cada pareja de documentos. 

#### Descripción del código

En cuanto a la distribución del código podemos decir que es un código bastante sencillo, ya que no cuenta con una estructura de directorios compleja, todo el código se aloja en la carpeta */src*. Dentro de esta carpeta podemos encontrar el fichero donde se encuentra el programa principal *main.py*, el que debemos ejecutar. Luego nos podemos encontrar con el fichero Recommender.py, donde se encuentra la clase que define el sistema de recomendación y sus métodos. Por último, nos encontramos con el fichero *GUI.py*, donde se encuentra la clase que define la interfaz gráfica del programa.


#### Visualización de documentación


Para la correcta visualización del despliegue de la documentación acceda al link adjunto en el repositorio de GitHub, esto lo llevará directamente a una pestaña del navegador donde puede consultar toda la documentación de nuestro programa.