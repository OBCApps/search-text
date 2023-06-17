import os
from collections import Counter
import json
from src.clean_tweets import generate_clean_tweets
import src.clean
import math

direction_dataset_clean = "clean_data_dev" # Direccion de donde esta guardado el dataset
nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio



def calculate_TF_IDF(tf):
    nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio
    lista = {}
    it = 0
    
    for i, doc in enumerate(tf):
        for term, freq in doc.items():
            # Aumentar el numero de ocurrencias en un documento
            tf_idf_weight = math.log10(1 + freq) * math.log10(len(tf) / sum(1 for doc in tf if term in doc) )
            
            if term in lista:
                lista[term] += f";{nanmes_docs[it]},{tf_idf_weight}" # Combinamos
            else:
                lista[term] = f"{nanmes_docs[it]},{tf_idf_weight}" #Cramos nuevo
        
        it += 1
        
        if it % 5 == 0:
            write_index(lista, it // 5)
            lista = {}
    
    write_index(lista, math.ceil(it / 5))
    



def write_index(data_write, num_index):
    ruta_archivo = f"prueba/index-{int(num_index)}.txt"
    print(f"Write File: {ruta_archivo}")
    
    with open(ruta_archivo, 'a', encoding='utf-8') as data:
        for term, value in data_write.items():
            data.write(f"{term}:{value}\n")



def create_invert_index():
    generate_clean_tweets()
    nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio
    all_jsns_frecuency = [] # Lista de cada jsn con su respectivas palabras y la cantidad que aparece
    for filename in nanmes_docs:
        lista = [] # Comentarios segun las veces que aparecen         
        #with open(direction_dataset_clean + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
        with open(direction_dataset_clean + '/' + filename, 'r', encoding='utf-8') as all_tweets:
            print(f"Load File: {direction_dataset_clean + '/' + filename}")
            all_tweets_dictionary = json.load(all_tweets)
            for tweet in all_tweets_dictionary: 
                temp = clean.clean_all(all_tweets_dictionary[tweet]) 
                lista.append(Counter(temp))
            all_jsns_frecuency.append( sum(lista, Counter()) )  # Jntamos las palabras que son repetidas
    
    calculate_TF_IDF(all_jsns_frecuency)


def create_index_of_web(data):
    generate_clean_tweets()
    
    all_jsns_frecuency = []
    lista = []
    for tweet in data: 
        temp = clean.clean_all(data[tweet]) # cargamos los datos en un diccionario, tambien el el load se le aplica una limpieza de mas cosas
        lista.append(Counter(temp))
    all_jsns_frecuency.append(sum(lista, Counter())) 
    calculate_TF_IDF(all_jsns_frecuency)

create_invert_index()
