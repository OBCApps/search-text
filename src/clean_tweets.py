

import os
import json
import errno

input_directory = "dataset\\data_elecciones"
curpath = os.path.abspath(os.curdir) # Almacena la ruta absoluta del directorio actual
nanmes_docs = os.listdir(input_directory) #Obtener la lista de los nombres de los archivos del dataset limpio



def gerenate_clean_tweets(): # Leemos el dataset y lo guardamos en un archivo limpio
    for filename in os.listdir(input_directory): # Recorremos todos los nombres
        if filename.endswith(".json") :  # Carga un archivo json
            with open(input_directory + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
                all_tweets_dictionary = json.load(all_tweets)
                result = {}
                for tweet in all_tweets_dictionary: # LA forma en que se guarda es en un diccionario donde solo queda el id y el text
                    result[tweet["id"]] = tweet["text"]
                file = "clean_data\\"+filename
                print("file")
                if not os.path.exists(os.path.dirname(file)):
                    try:
                        os.makedirs(os.path.dirname(file)) # Verifica si el directorio existe
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(file, "w", encoding='utf-8') as clean_file:
                    clean_file.write(json.dumps(result)) 

def main():
    print("... Limpiando tweets ... ")
    gerenate_clean_tweets()
    print("... Limpieza finalizada ... ")

main()
