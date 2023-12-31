import os
from collections import Counter
import json
#from clean_tweets import generate_clean_tweets,generate_clean_tweets_web, load_file
from src.clean_tweets import generate_clean_tweets,generate_clean_tweets_web
from  src.clean import clean_all , clean_all2
#from  clean import clean_all, clean_all2
import math

direction_dataset_clean = "./src/clean_data"
#direction_dataset_clean = "clean_data_dev" # Direccion de donde esta guardado el dataset
#nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio
ruta_archivo = "./src/indexs-local"

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
    #ruta_archivo = f"prueba/index-{int(num_index)}.txt"
    
    print(f"Write File: {ruta_archivo}")
    if not os.path.exists(ruta_archivo):
        os.makedirs(ruta_archivo)
    with open(f"{ruta_archivo}/index{int(num_index)}.txt", 'a', encoding='utf-8') as data:
        for term, value in data_write.items():
            data.write(f"{term}:{value}\n")

def load_jsons_frecuency():
    all_jsns_frecuency = [] # Lista de cada jsn con su respectivas palabras y la cantidad que aparece

    for filename in nanmes_docs:
        lista = [] # Comentarios segun las veces que aparecen         
        #with open(direction_dataset_clean + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
        with open(direction_dataset_clean + '/' + filename, 'r', encoding='utf-8') as all_tweets:
            print(f"Load File: {direction_dataset_clean + '/' + filename}")
            all_tweets_dictionary = json.load(all_tweets)
            for tweet in all_tweets_dictionary: 
                temp = clean_all2(all_tweets_dictionary[tweet]) 
                lista.append(Counter(temp))
            all_jsns_frecuency.append( sum(lista, Counter()) )
    return all_jsns_frecuency

def create_invert_index():
    # Debe escribir en indexs-local
    generate_clean_tweets()
    print("... Construcción Indice Local.. ")
    global ruta_archivo
    ruta_archivo = "./src/indexs-local"
    
    global direction_dataset_clean
    direction_dataset_clean = "./src/clean_data"

    global nanmes_docs
    nanmes_docs = os.listdir(direction_dataset_clean) 
    
    all_jsns_frecuency = load_jsons_frecuency()
    
    calculate_TF_IDF(all_jsns_frecuency)
    print("... Construcción Local Finalizada .. ")


def create_index_of_web(data):
    generate_clean_tweets_web(data)
#def create_index_of_web():
    global ruta_archivo
    ruta_archivo = "./src/indexs-web"
    
    global direction_dataset_clean
    direction_dataset_clean = "./src/clean_data_dev"
    
    global nanmes_docs
    nanmes_docs = os.listdir(direction_dataset_clean) 
    
    print("... Construcción Indice Web.. ")
    all_jsns_frecuency = [] # Lista de cada jsn con su respectivas palabras y la cantidad que aparece

    for filename in nanmes_docs:
        lista = [] # Comentarios segun las veces que aparecen         
        #with open(direction_dataset_clean + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
        with open(direction_dataset_clean + '/' + filename, 'r', encoding='utf-8') as all_tweets:
            print(f"Load File: {direction_dataset_clean + '/' + filename}")
            all_tweets_dictionary = json.load(all_tweets)
            for tweet in all_tweets_dictionary: 
                temp = clean_all2(all_tweets_dictionary[tweet]) 
                lista.append(Counter(temp))
            all_jsns_frecuency.append( sum(lista, Counter()) )  # Jnt
    calculate_TF_IDF(all_jsns_frecuency)
    print("... Construcción Web Finalizada .. ")

#create_invert_index()
# data = []
# for filename in os.listdir("dataset\\data_elecciones_dev"):
#     if filename.endswith(".json"):
#         input_file = os.path.join("dataset\\data_elecciones_dev", filename)
#         tweets = load_file(input_file)
#         data.append(tweets)
        

# create_index_of_web(data)