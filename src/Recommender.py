import string
import re
import json
import math
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem
from PyQt5.QtGui import QColor

# Ojito esta es curiosa
# from pandasgui import show


class Recommender:
  punctuation = ',.!?;:"()[]{}'
  def __init__(self, documents_filename, stop_words_filename, corpus_filename):
    self.frequencies = self.load_data(documents_filename, stop_words_filename, corpus_filename)
  


  def load_data(self, documents_filename, stop_words_filename, corpus_filename):
    list_term_count = []
    stop_word_list = []
    
    # Guardamos todas las stop_words
    with open(stop_words_filename, "r") as stop_word_file_system:
      stop_word_list = [x.strip() for x in stop_word_file_system.readlines()]
    
    # Guardamos los elementos de lematización
    with open(corpus_filename, "r") as corpus_file_system:
      corpus_list = json.load(corpus_file_system)
    
    with open(documents_filename, "r") as document_file_system:
      for line in document_file_system.readlines():
        # Elimina los signos de puntuación
        line = re.sub(r'[^\w\s\']', '', line)
        # Pasa todo a minúsculas
        line = line.lower()
        document = dict()
        for element in line.split():
          # Elimina las palabras que se encuentren en stop_words
          if element in stop_word_list:
            continue

          # Sacamos la frecuencia de las palabras
          if element in corpus_list:
            element = corpus_list[element]
          if element in document:
            document[element] += 1
          else:
            document[element] = 1
        list_term_count.append(document)
    return list_term_count
  
  
  
  
  def calculate_df(self):
    self.df = dict()
    for dictionary in self.frequencies:
      for element in dictionary:
        if element in self.df:
          self.df[element] += dictionary[element]
        else:
          self.df[element] = dictionary[element]
    for word in self.df:
      for i in range(len(self.frequencies)):
        if word in self.frequencies[i]:
          continue
        else:
          self.frequencies[i][word] = 0 
    return self.df




  def calculate_tf(self):
    self.tf = []
    for dictionary in self.frequencies:
      aux = dict()
      for element in dictionary:
        if dictionary[element] == 0:
          aux[element] = 0
        else:
          aux[element] = 1 + math.log10(dictionary[element])
      self.tf.append(aux)
    return self.tf




  def calculate_idf(self):
    self.idf = dict()
    for element in self.df:
      self.idf[element] = math.log10(len(self.frequencies)/self.df[element])
    return self.idf
  
  
  

  def calculate_length_vector(self):
    self.length_vector = []
    for dictionary in self.tf:
      aux = 0
      for element in dictionary:
        aux += dictionary[element]**2
      self.length_vector.append(math.sqrt(aux))
    return self.length_vector



  def calculate_tf_idf(self):
    self.tf_idf = []
    for dictionary in self.tf:
      aux = dict()
      for element in dictionary:
        if dictionary[element] > 0:
          aux[element] = 1 + math.log10(dictionary[element])
        else:
          aux[element] = 0
      self.tf_idf.append(aux)
    return self.tf_idf
  
  
  
  
  
  def plot_count_table(self):
    app = QApplication([])
    win = QWidget()
    scroll = QScrollArea()
    layout = QVBoxLayout()
    table = QTableWidget()
    scroll.setWidget(table)
    layout.addWidget(table)
    win.setLayout(layout) 
    win.resize(800, 600)  # Establece el tamaño inicial de la ventana a 800x600 píxeles
    data = {  key: [] for key in self.df}
    aux = []
    for key in data:
      for diccionario in self.frequencies:
        value = diccionario.get(key)  # Obtenemos el valor de la clave "key"
        data[key].append(value)
      data[key].append(self.df[key])
        
    
    # data["DF_RESULT"] = [self.df[key] for key in self.df]
        
    
    data_frame = pd.DataFrame(data)
  
    table.setColumnCount(len(data_frame.columns))
    table.setRowCount(len(data_frame.index))
    # permitimos que la tabla se estire para llenar el espacio disponible
    table.horizontalHeader().setStretchLastSection(True)
    table.verticalHeader().setStretchLastSection(True)
    table.setHorizontalHeaderLabels(data_frame.columns)  # Establece los nombres de las columnas
    table.setVerticalHeaderLabels([ f"Article {i}" for i in range(len(data_frame.index)-1)] + ["DF"])  # Establece los nombres de las columnas
    table.horizontalHeader().setStyleSheet("QHeaderView::section {background-color:rgb( 53, 180, 19)}")  # Establece el color de fondo de las cabeceras de las columnas
    
    for i in range(len(data_frame.index)):
      for j in range(len(data_frame.columns)):
        item = QTableWidgetItem(str(data_frame.iloc[i, j]))
        if i % 2 == 0:
          item.setBackground(QColor(166, 255, 142))  # Fondo azul claro para filas pares

        table.setItem(i, j, item)
    win.show()
    app.exec_()



  # def __str__(self):
  #   result = '\n'
  #   for element in self.df:
  #     result += f'{element:<15}'
    
  #   result += '\n'

  #   for i in range(len(self.frequencies)):
  #     # result += f'\nFor line {i}'
  #     for word in self.frequencies[i]:
  #       result += f'{self.frequencies[i][word]:<5}'
      
  #   # result += '\nDF\n'
  #   # for word in self.df:
  #   #   result += f"\n    {word:<15} --> {self.df[word]:<6}"
  #   return result