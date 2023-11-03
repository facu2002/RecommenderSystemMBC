from Recommender import Recommender
from GUI import GUI
from PyQt5.QtWidgets import QApplication
import sys
import argparse
import time

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
elif str(args.language) == 'es':
  stop_words_filename = f"./data/stop_words/stop-words-es.txt"
  corpus_filename = f"./data/corpus/corpus-es.txt"

# Caso en el que se introduce un idioma diferente
else:
  print("Error: language not found")
  sys.exit()



# Iniciamos el tiempo
start_time = time.time()
recommender = Recommender(documents_filename, stop_words_filename, corpus_filename)
# Detenemos el tiempo
end_time = time.time()
# Calculamos el tiempo de ejecución
total_time = end_time - start_time
print(f"The execution time was {total_time:.4f} seconds")



if str(args.print) == 'yes':
  start_time = time.time()
  app = QApplication(sys.argv)
  ventana = GUI(recommender)
  end_time = time.time()
  total_time = end_time - start_time
  print(f"The time to graph it is {total_time:.4f} seconds")
  sys.exit(app.exec_())

elif str(args.print) == 'no':
  start_time = time.time()
  print(recommender)
  end_time = time.time()
  total_time = end_time - start_time
  print(f"The time to print it is {total_time:.4f} seconds")
  
  
else:
  print("Error: incorrect option")
  sys.exit()