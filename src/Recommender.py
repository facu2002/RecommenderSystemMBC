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
    self.calculate_df()
    self.calculate_tf()
    self.calculate_idf()
    self.calculate_length_vector()
    self.calculate_tf_idf()


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
    """
    Function that calculates the document frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Returns a dictionary with the document frequency of the words in the documents.
    """
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
    """
    Function that calculates the term frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the term frequency of the words in the documents.
    """
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
    """
    Function that calculates the inverse document frequency of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the inverse document frequency of the words in the documents.
    """
    self.idf = dict()
    for element in self.df:
      self.idf[element] = math.log10(len(self.frequencies)/self.df[element])
    return self.idf

  

  def calculate_length_vector(self):
    """
    Function that calculates the length of the vectors of the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        List with the length of the vectors of the documents.
    """
    self.length_vector = []
    for dictionary in self.tf:
      aux = 0
      for element in dictionary:
        aux += dictionary[element]**2
      self.length_vector.append(math.sqrt(aux))
    return self.length_vector



  def calculate_tf_idf(self):
    """
    Function that calculates the tf_idf of the words in the documents.
    Args:
        self: argument that refers to the created instance of the class.
    Returns:
        Dictionary with the tf_idf of the words in the documents.
    """
    self.tf_idf = []
    i = 0
    for dictionary in self.tf:
      aux = dict()
      for element in dictionary:
        if dictionary[element] > 0:
          aux[element] = dictionary[element] / self.length_vector[i]
        else:
          aux[element] = 0
      self.tf_idf.append(aux)
      i += 1
    return self.tf_idf



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
    if len(dict1) == len(dict2):
      for i in dict1:
        result += dict1[i] * dict2[i]
      return result
    return -1



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
