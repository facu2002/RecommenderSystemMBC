from Recommender import Recommender


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
# for i in range(len(recommender.frequencies)):
#   print("La linea ", i)
#   for element in recommender.frequencies[i]:
#     print("   Veamos que", element, recommender.frequencies[i][element] )

recommender.calculate_df()

recommender.calculate_tf()
recommender.calculate_idf()
print(recommender.idf)
recommender.calculate_length_vector()
recommender.calculate_tf_idf()


# print(recommender.df)
# print(recommender.tf)   

# recommender.plot_count_table()