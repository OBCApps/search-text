import os
from collections import Counter
import json

import clean
import math

direction_dataset_clean = "clean_data" # Direccion de donde esta guardado el dataset
curpath = os.path.abspath(os.curdir) # Almacena la ruta absoluta del directorio actual
nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio




def merge(lista): # Junta todos las palabras con sus repeticiones, si hay quienes se repiten se junta y se suma la cantidad de veces que se repite    
    return sum(lista, Counter())



def calculate_TF_IDF(all_letter_frequencies):
    term_document_map = {}  # Diccionario para almacenar los términos y sus valores TF-IDF
    document_index = 0

    for document in all_letter_frequencies:
        for letter, frequency in document.items():
            tfidf = math.log(1 + frequency) * math.log(len(all_letter_frequencies) / calculate_DF(letter, all_letter_frequencies))
            
            if letter in term_document_map:
                term_document_map[letter] = str(term_document_map[letter]) + ";" + str(document_index) + "," + str(tfidf)
            else:
                term_document_map[letter] = str(document_index) + "," + str(tfidf)
        
        document_index += 1
        
        if document_index % 5 == 0:
            write_index(term_document_map, document_index / 5)
            term_document_map = {}
    
    
    if term_document_map:
        write_index(term_document_map, math.ceil(document_index / 5))



def calculate_DF(word, lista):  
    c = 0
    for i in lista:
        if word in i:
            c += 1
    return c

def write_index(data_write, num_index): # Crea el archivo de indice, donde X es el numero d ebloque
    #ruta_archivo = "prueba\\index-" + str(int(num_index)) + ".txt"  
    ruta_archivo = "prueba/index-" + str(int(num_index)) + ".txt"  
    print(f"write: {ruta_archivo}")
    with open(ruta_archivo, 'a', encoding='utf-8') as data: 
        for k in data_write:
            data.write(k + ':'+ data_write[k] + '\n')
                    


def create_invert_index():
    all_jsns_frecuency = [] # Lista de cada jsn con su respectivas palabras y la cantidad que aparece
    for filename in nanmes_docs:
        lista = [] # Comentarios segun las veces que aparecen         
        #with open(direction_dataset_clean + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
        with open(direction_dataset_clean + '/' + filename, 'r', encoding='utf-8') as all_tweets:
            all_tweets_dictionary = json.load(all_tweets)
            for tweet in all_tweets_dictionary: 
                temp = clean.clean_all(all_tweets_dictionary[tweet]) # cargamos los datos en un diccionario, tambien el el load se le aplica una limpieza de mas cosas
                lista.append(Counter(temp))
            all_jsns_frecuency.append(merge(lista)) 
    calculate_TF_IDF(all_jsns_frecuency)

def create_index_of_web(data):
    all_jsns_frecuency = []
    lista = []
    for tweet in data: 
        temp = clean.clean_all(data[tweet]) # cargamos los datos en un diccionario, tambien el el load se le aplica una limpieza de mas cosas
        lista.append(Counter(temp))
    all_jsns_frecuency.append(merge(lista)) 
    calculate_TF_IDF(all_jsns_frecuency)

#create_invert_index()
