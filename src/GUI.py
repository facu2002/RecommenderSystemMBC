import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QHeaderView, QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QTabWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

from Recommender import Recommender


class GUI(QWidget):
  
  def __init__(self, recommender: Recommender):
    """
    Constructor of the GUI class, responsible for creating instances for represent tables
    Args:
        self: argument that refers to the created instance of the class.
        recommender: object of the Recommender class that we want to print.
    """
    super().__init__()
    self.initUI(recommender)



  def initUI(self, recommender: Recommender):
    """
    Function that initializes what is necessary to print the tables.
    Args:
        self: argument that refers to the created instance of the class.
        recommender: object of the Recommender class that we want to print.
    """    
    # Crear el widget de pestañas
    tab_widget = QTabWidget(self)
    
    # Crear la primera tabla y agregar datos de ejemplo
    for index, article in enumerate(recommender.frequencies):
      table = self.create_table(article, index, recommender)
      label = self.print_similarity(index, recommender)
      # Crear un widget contenedor
      hbox = QHBoxLayout(self)
      widget_contenedor = QWidget()

      # Establecer los stretch factors para definir la relación de tamaño
      hbox.addWidget(table, 3)  # La tabla ocupará 2/3 del espacio
      hbox.addWidget(label, 1)  # El label ocupará 1/3 del espacio

      # Establecer el diseño del widget contenedor
      widget_contenedor.setLayout(hbox)
      tab_widget.addTab(widget_contenedor, f"Document {index}")
        
    # Diseño del diseño principal
    layout = QVBoxLayout(self)
    layout.addWidget(tab_widget)
    self.setLayout(layout)

    self.setWindowTitle('Recommender Content-Based Models')
    self.setGeometry(300, 150, 1000, 600)
    
    # Establecer el icono de la aplicación
    self.setWindowIcon(QIcon('src/icon.svg'))
    self.show()



  def create_table(self, article, num_article, recommender: Recommender):
    """
    Function that creates the table with all the data.
    Args:
        self: argument that refers to the created instance of the class.
        article: document that we are analyzing.
        num_article: number of the document that we are analyzing.
        recommender: object of the Recommender class that we want to print.
    Returns:
        The table with all the information.
    """
    table = QTableWidget(self)
    table.setColumnCount(6)
    table.setRowCount(len(article))
    table.setHorizontalHeaderLabels(["Term", "Frequency", "DF", "TF", "IDF", "TF-IDF"])
    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Stretch)
    # setColumnWidth(index_column, size)
    table.setColumnWidth(3, 200)
    table.setColumnWidth(4, 200)
    # se dimensiona las columnas para que se ajusten al tamaño de la ventana
    # se establece el tamaño de las filas
    table.verticalHeader().setDefaultSectionSize(20)
    # se establece el tamaño de las columnas
    table.horizontalHeader().setDefaultSectionSize(180)
    table.setStyleSheet(
      
      """
      QTableWidget {
          background-color: #ffffff; /* Color de fondo de la tabla (blanco) */
          alternate-background-color: #f0f0f5; /* Color de fondo de las filas alternas (morado claro) */
          color: #333; /* Color del texto */
      }
      QHeaderView::section {
          background-color: #800080; /* Color de fondo del encabezado (morado) */
          color: white; /* Color del texto del encabezado */
      }
      QTableWidget::item:hover {
          background-color: #0078d4; /* Color de fondo cuando una celda está seleccionada (azul) */
      }
      """

    )
    # centramos los valores en las celdas
    for index, term in enumerate(article):
      # Termino
      item = QTableWidgetItem(str(term))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 0, item)
      # Apariciones
      item = QTableWidgetItem(str(article[term]))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 1, item)
      # DF
      item = QTableWidgetItem(str(recommender.df[term]))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 2, item)
      # TF
      item = QTableWidgetItem(str(recommender.tf[num_article][term]))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 3, item)
      # IDF
      item = QTableWidgetItem(str(recommender.idf[term]))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 4, item)
      # TF-IDF
      item = QTableWidgetItem(str(recommender.tf_idf[num_article][term]))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(index, 5, item)
    return table



  def print_similarity(self, num_article, recommender):
    """
    Function that prints the data related to the similarities in the form of a table.
    Args:
        self: argument that refers to the created instance of the class.
        num_article: number of the document that we are analyzing.
        recommender: object of the Recommender class that we want to print.
    Returns:
       The table with the data of the similarities.
    """
    similarities = recommender.calculate_similarity(num_article)
    table = QTableWidget(self)
    table.setColumnCount(2)
    table.setRowCount(len(similarities))
    table.setHorizontalHeaderLabels(["Documents", "Similarity"])
    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Stretch)
    table.setColumnWidth(0, 100)
    table.setColumnWidth(1, 200)
    index = 0
    for i, similarity in enumerate(similarities):
      if index == num_article:
        index += 1
      # Documentos
      item = QTableWidgetItem(f"COS({num_article}, {index})")
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(i, 0, item)
      # Similaridad
      item = QTableWidgetItem(str(similarity))
      item.setTextAlignment(0x0004 | 0x0080)
      table.setItem(i, 1, item)
      index += 1
    return table