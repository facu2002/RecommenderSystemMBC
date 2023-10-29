import string
import re
import json
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem
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
      print(type(corpus_list))
    
    
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
    for key in data:
      for diccionario in self.frequencies:
        value = diccionario.get(key)  # Obtenemos el valor de la clave "key"
        data[key].append(value)
    
    df = pd.DataFrame(data)
  
    table.setColumnCount(len(df.columns))
    table.setRowCount(len(df.index))
    table.setHorizontalHeaderLabels(df.columns)  # Establece los nombres de las columnas

    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))

    win.show()
    app.exec_()

  def __str__(self):
    result = '\n'
    for element in self.df:
      result += f'{element:<15}'
    
    result += '\n'

    for i in range(len(self.frequencies)):
      # result += f'\nFor line {i}'
      for word in self.frequencies[i]:
        result += f'{self.frequencies[i][word]:<5}'
      
    # result += '\nDF\n'
    # for word in self.df:
    #   result += f"\n    {word:<15} --> {self.df[word]:<6}"
    return result