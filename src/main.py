from Recommender import Recommender
from tables import TablasApp
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
documents_filename = f"./data/documents/documents-01.txt"



recommender = Recommender(documents_filename, stop_words_filename, corpus_filename)

recommender.calculate_df()

recommender.calculate_tf()

recommender.calculate_idf()

recommender.calculate_length_vector()

recommender.calculate_tf_idf()

app = QApplication(sys.argv)

ventana = TablasApp(recommender)

sys.exit(app.exec_())
