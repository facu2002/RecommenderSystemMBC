from Recommender import Recommender
from GUI import GUI
from PyQt5.QtWidgets import QApplication
import sys
import argparse

if len(sys.argv) != 1:
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--filename", required=True, help="entering the name of the file you want to analyze")
  parser.add_argument("-l", "--language", required=True, help="entering the language of the document")
  parser.add_argument("-p", "--print", required=True, help="enter whether you want to print the result graphically or not")
  
  args = parser.parse_args()
  # Leemos el fichero de entrada de datos
  documents_filename = f"./data/documents/{str(args.filename)}"


# Caso en el que se introduce un documento en inglés
if str(args.language) == 'en':
  stop_words_filename = f"./data/stop_words/stop-words-en.txt"
  corpus_filename = f"./data/corpus/corpus-en.txt"

# Caso en el que se introduce un documento en español
if str(args.language) == 'es':
  stop_words_filename = f"./data/stop_words/stop-words-es.txt"
  corpus_filename = f"./data/corpus/corpus-es.txt"


recommender = Recommender(documents_filename, stop_words_filename, corpus_filename)

if str(args.print) == 'yes':
  app = QApplication(sys.argv)
  ventana = GUI(recommender)
  sys.exit(app.exec_())

if str(args.print) == 'no':
  print(recommender)