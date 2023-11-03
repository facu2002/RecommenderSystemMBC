import re
import json
import math



class Recommender:


  def __init__(self, documents_filename, stop_words_filename, corpus_filename):
    """
    Constructor of the Recommender class, responsible for creating instances of the class
    Args:
        self: argument that refers to the created instance of the class.
        documents_filename: name of the file that contains the documents.
        stop_words_filename: name of the file that contains the stop words.
        corpus_filename: name of the file that contains the corpus (for the lemmatization).
    Returns:
        Returns the created instance of the Recommender class.
    """
    self.frequencies = self.load_data(documents_filename, stop_words_filename, corpus_filename)
    self.df = self.calculate_df()
    self.tf = self.calculate_tf()
    self.idf = self.calculate_idf()
    self.length_vector = self.calculate_length_vector()
    self.tf_idf = self.calculate_tf_idf()
    
  def __str__(self):
    result = ""
    result += "\nFrequencies:\n"
    for index, i in enumerate(self.frequencies):
      result += "Document " + str(index) + "\n"
      result += str(i) + "\n\n"
    result += "\nDF:\n"
    for i in self.df:
      result += str(i) + " = " + str(self.df[i]) + "\n"
    result += "\nTF:\n"
    for i in self.tf:
      result += str(i) + "\n"
    result += "\nIDF:\n"
    for i in self.idf:
      result += str(i) + " = " + str(self.idf[i]) + "\n"
    result += "\nLength Vector:\n"
    for i in self.length_vector:
      result += str(i) + "\n"
    result += "\nTF-IDF:\n"
    for i in self.tf_idf:
      result += str(i) + "\n"
    result += "\nSimilarity:\n"
    for i in range(len(self.tf_idf)):
      result += str(self.calculate_similarity(i)) + "\n"
    result += "\n REMEMBER: Use de GUI to see the data in a better way.\n"
    return result
  
      


  def load_data(self, documents_filename, stop_words_filename, corpus_filename):
    """
    Function that loads the data from the files and creates the strcutures needed for the recommender.
    Args:
        documents_filename: name of the file that contains the documents.
        stop_words_filename: name of the file that contains the stop words.
        corpus_filename: name of the file that contains the corpus (for the lemmatization).

    Returns:
        Returns a list of dictionaries, where each dictionary contains the frequency of the words in a document.
    """
    list_term_count = []
    stop_word_list = []
    
    # Guardamos todas las stop_words
    with open(stop_words_filename, "r") as stop_word_file_system:
      stop_word_list = [x.strip() for x in stop_word_file_system.readlines()]
    
    # Guardamos los elementos de lematización
    with open(corpus_filename, "r") as corpus_file_system:
      corpus_list = json.load(corpus_file_system)
    
    with open(documents_filename, "r", encoding='utf-8') as document_file_system:
      line = document_file_system.readline()
      while line:
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
        line = document_file_system.readline()
    return list_term_count



  def calculate_df(self):
    """
    Function that calculates the document frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Returns a dictionary with the document frequency of the words in the documents.
    """
    df = dict()
    for dictionary in self.frequencies:
      for element in dictionary:
        if element in df:
          df[element] += dictionary[element]
        else:
          df[element] = dictionary[element]
    # for word in df:
    #   for i in range(len(self.frequencies)):
    #     if word in self.frequencies[i]:
    #       continue
    #     else:
    #       self.frequencies[i][word] = 0 
    return df



  def calculate_tf(self):
    """
    Function that calculates the term frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the term frequency of the words in the documents.
    """
    tf = []
    for dictionary in self.frequencies:
      aux = dict()
      for element in dictionary:
        if dictionary[element] == 0:
          aux[element] = 0
        else:
          aux[element] = 1 + math.log10(dictionary[element])
      tf.append(aux)
    return tf



  def calculate_idf(self):
    """
    Function that calculates the inverse document frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the inverse document frequency of the words in the documents.
    """
    idf = dict()
    for element in self.df:
      idf[element] = math.log10(len(self.frequencies)/self.df[element])
    return idf

  

  def calculate_length_vector(self):
    """
    Function that calculates the length of the vectors of the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        List with the length of the vectors of the documents.
    """
    length_vector = []
    for dictionary in self.tf:
      aux = 0
      for element in dictionary:
        aux += dictionary[element]**2
      length_vector.append(math.sqrt(aux))
    return length_vector



  def calculate_tf_idf(self):
    """
    Function that calculates the tf_idf of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the tf_idf of the words in the documents.
    """
    tf_idf = []
    i = 0
    for dictionary in self.tf:
      aux = dict()
      for element in dictionary:
        if dictionary[element] > 0:
          aux[element] = dictionary[element] / self.length_vector[i]
        else:
          aux[element] = 0
      tf_idf.append(aux)
      i += 1
    return tf_idf



  def calculate_cosine(self, dict1, dict2):
    """
    Function that calculates the cosine of two vectors (documents).
    Args:
        self: argument that refers to the created instance of the class.
        dict1: list of the values of the normalized vector of the first document.
        dict2: list of the values of the normalized vector of the second document.
    Returns:
        Value of the cosine of the two vectors.
    """  
    result = 0
    terms = list(set(dict1) & set(dict2))
    for i in terms:
      result += dict1[i] * dict2[i]
    return result



  def calculate_similarity(self, document):
    """
    Function that calculates the similarity of a document with the rest of the documents.
    Args:
        self: argument that refers to the created instance of the class.
        document: number of the document to calculate the similarity with the rest of the documents.
    Returns:
        List with the similarity of the document with the rest of the documents.
    """
    result = []
    for i in range(len(self.tf_idf)):
      if(document != i):
        result.append(self.calculate_cosine(self.tf_idf[document], self.tf_idf[i]))
      
    return result 
