from Recommender import Recommender
from GUI import GUI
from PyQt5.QtWidgets import QApplication
import sys


#el usuario debe introducir el idioma del documento entonces nosotros elegimos entre

# si posix == en
# #ingles
stop_words_filename = f"./data/stop_words/stop-words-en.txt"
corpus_filename = f"./data/corpus/corpus-en.txt"

# si posix == es
# #español
# stop_words_filename = f"./data/stop_words/stop-words-es.txt"
# corpus_filename = f"./data/corpus/corpus-es.txt"

# el unico parametro que debe introducir el usuario es documents_filename
documents_filename = f"./data/documents/documents-03.txt"



recommender = Recommender(documents_filename, stop_words_filename, corpus_filename)

app = QApplication(sys.argv)

ventana = GUI(recommender)

sys.exit(app.exec_())

