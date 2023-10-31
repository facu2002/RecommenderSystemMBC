import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QHeaderView, QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QTabWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

from Recommender import Recommender


class GUI(QWidget):
  
  def __init__(self, recommender: Recommender):
    super().__init__()
    
   
    self.initUI(recommender)
  
  def initUI(self, recommender: Recommender):
    # Crear el widget de pestañas
    tab_widget = QTabWidget(self)
    
    # Crear la primera tabla y agregar datos de ejemplo
    for index, article in enumerate(recommender.frequencies):
      table = self.create_table(article, index, recommender)
      label = self.create_similarity(index, recommender)
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
    
    
    # poner el boton de cerrar arriba a la derecha
    close_button = QPushButton("", self)
    icon = QIcon("src/close.svg")
    
    close_button.setIcon(icon)
    close_button.setIconSize(QSize(20, 20))
    close_button.setFixedSize(QSize(30, 30))
    close_button.setStyleSheet("QPushButton { background-color: #ffffff; border: none; } QPushButton:hover { background-color: #ff0000; }")
    close_button.clicked.connect(self.close)
    layout.addWidget(close_button, alignment=Qt.AlignRight)
    layout.addWidget(tab_widget)

    self.setLayout(layout)

    self.setWindowTitle('Recommender Content-Based Models')
    self.showFullScreen()
    
    
    
    button = QPushButton("Cerrar Ventana", self)
    button.clicked.connect(self.close)
    
    # Establecer el icono de la aplicación
    self.setWindowIcon(QIcon('src/icon.svg'))
    self.show()



  def create_table(self, article, num_article, recommender: Recommender):
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
  
  def create_similarity(self, num_article, recommender):
    
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
    # # se establece el tamaño de las filas
    # table.verticalHeader().setDefaultSectionSize(20)
    # # se establece el tamaño de las columnas
    # table.horizontalHeader().setDefaultSectionSize(100)
  
  # def create_similarity(self, num_article, recommender):
  #   result = ""
  #   index = 0
  #   for similarity in recommender.calculate_similarity(num_article):
  #     if index == num_article:
  #       index += 1
  #     result += f"COS({num_article}, {index}) = {similarity}\n"
  #     index += 1
  #   label = QLabel(result)
  #   label.setStyleSheet(
  #     "QLabel {"
  #     "background-color: #ffffff;" 
  #     "color: #000000;"            
  #     "border: 2px solid #2980b9;" 
  #     "border-radius: 5px;"        
  #     "padding: 5px;"
  #     "font-size: 15px;"
  #     "font-weight: bold;"         
  #     "}"
  #   )
  #   return label


# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   ventana = TablasApp()
#   sys.exit(app.exec_())
