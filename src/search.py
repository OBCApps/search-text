import os

from src.clean import clean_all
import json
from collections import Counter
import math
from nltk.stem.snowball import SnowballStemmer
import nltk
nltk.download('punkt')

direction_dataset_clean = "./src/clean_data" # Leemos del dataset ya limpio
nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio

direction_indexs = "./src/indexs/index"
ind = {}  



# Busqueda
def read_inverted(): #Lee los indices, y retorna un diccionario de indices(Ya une con todos los archivos)
    print("readInverted():")    
    cont = 1
    
    while(True): # Lee los indices invertidos
        pat = direction_indexs + str(cont)+".txt"
        if os.path.exists(pat): # Mientras existe el archivo
            with open(pat, 'r', encoding="ISO-8859-1") as indice: # Abre el archivo
                #print("leyendo indices: " , f)
                for line in enumerate(indice): 

                    pair = str(line[:len(line)-2]).split(':') # No leemos el \n

                    if pair[0] in ind:
                        ind[pair[0]] = str(ind[pair[0]]) + ";" + str(pair[1]) #Si es que ya existe, concatenamos los documentos   
                    else:
                        if len(pair) >= 2:
                            ind[pair[0]] = str(pair[1])
                        #ind[pair[0]] = str(pair[1]) # Si no existe crea uno nuevo
            cont += 1
        else:
            break
    return ind

# Busqueda
def get_frecuency(palabras): # Hace limpieza, filtra palabras clave, retrona frecuencias
    stemmer = SnowballStemmer('spanish') # Cojemos las palabras clave    
    roots = [stemmer.stem(i) for i in palabras] # Convertimos todas las palbras en su base raiz
    return len(roots),Counter(roots) 

# Busqueda
def documentos_relevantes(query, k): # Retorna una lista ordenada de los documentos mas relevantes en una consulta (query)
    #cantidadTF, tf = get_frecuency(query) # Palabras con sus frecuencias (Diccionario )
    tf = get_frecuency(query)
    dic = {} 
    
    inverted = read_inverted()# Indices, palabras y documentos (Diccionario)
    
    scores = {}
    lenght1 = {}
    # aseguramos que los puntajes y las longitudes se inicien en 0 antes de calcularlos 
    for i in nanmes_docs: # Recorremos los nombres de los archivos limpios
        scores[i] = 0
        lenght1[i] = 0
    
    lenght2 = 0 # Para calcular la suma de los cuadrados de los pesos
    # REcorremos las palabras con sus frecuencias
    for i in tf:
        # math.log(1 + tf[i]): Aplica una transformación logarítmica a la frecuencia del término en el documento. El 1 es para evitar tomar el logaritmo de cero en caso de que el término no aparezca en el documento.
        # math.log(len(archivos)/df_ind(i, inverted)) : Calcula la frecuencia inversa del termino , para reducir la importancia del termino que aparecen en muchos documentos
         
        wtfidf = math.log(1 + tf[i]) * math.log(len(nanmes_docs) / len(inverted[i].split(';'))    ) 
        #wtfidf = math.log(1 + tf[i] / cantidadTF ) * math.log(len(nanmes_docs) / len(inverted[i].split(';'))    ) 
        # Guaramos en el diccionario su peso calculado
        dic[i] = wtfidf

        lenght2 = lenght2 + wtfidf**2 # Calcular la suma de cuadrados

        values = inverted[i].split(';') #lista de palabras y documentso
        for j in values:  
            j = j.split(',') # Divido los docuentos
            lenght1[j[0]] = lenght1[j[0]] + float(j[1])**2
            scores[j[0]] = scores[j[0]] + float(j[1])*wtfidf
    lenght2 = lenght2**0.5
    for i in lenght1:
        if lenght1[i] != 0:
            lenght1[i] = lenght1[i]**0.5
    for i in scores:
        if lenght1[i] != 0:
            scores[i] = scores[i]/(lenght1[i]*lenght2)
    orderedDic = sorted(scores.items(), key=lambda it: it[1], reverse=True)
    return orderedDic
""" def documentos_relevantes(query, k):
    tf = obtener_frecuencia(query)
    diccionario_pesos = calcular_pesos_tf_idf(tf)
    scores = calcular_scores(diccionario_pesos)
    documentos_ordenados = ordenar_documentos(scores)
    return documentos_ordenados[:k]

def obtener_frecuencia(query):
    frecuencia = {}
    for palabra in query:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def calcular_pesos_tf_idf(tf):
    diccionario_pesos = {}
    total_documentos = len(nanmes_docs)
    for termino, frecuencia in tf.items():
        peso_tf = 1 + math.log(frecuencia)
        idf = math.log(total_documentos / obtener_df(termino))
        peso_tfidf = peso_tf * idf
        diccionario_pesos[termino] = peso_tfidf
    return diccionario_pesos

def calcular_scores(diccionario_pesos):
    scores = {documento: 0 for documento in nanmes_docs}
    for termino, peso_tfidf in diccionario_pesos.items():
        valores = inverted[termino].split(';')
        for valor in valores:
            documento, peso = valor.split(',')
            scores[documento] += float(peso) * peso_tfidf
    return scores

def ordenar_documentos(scores):
    documentos_ordenados = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return documentos_ordenados

def obtener_df(termino):
    df = 0
    for valores in inverted.values():
        documentos = valores.split(';')
        for valor in documentos:
            documento, _ = valor.split(',')
            if documento == termino:
                df += 1
                break
    return df
 """



def search_valid(documentos , palabras):        
    """
    - leer los documentos con su orden de relevancia, leemos los documentos , 
    recorremos las palabras a buscar limpias, 
    """    
    lista = []        
    for i in documentos:
        with open(direction_dataset_clean + '/' + i[0], 'r', encoding='utf-8' ) as documentos_encontrados:
            relevantes_cargados= json.load(documentos_encontrados)
            for letter in palabras: # Query
                for twet in relevantes_cargados:
                    temp = relevantes_cargados[twet]
                    if temp.find(letter) != -1: # Retorna -1 si no lo encuentra
                        lista.append( {twet , relevantes_cargados[twet] })# Agregamos el tweet con su valor
                        #lista.append( {twet})
    return lista
                    
# Busqueda
def search_tweet(query, k): # Retorna los tweets encontrados
    print("search_tweet(query, k):")
    documentos = documentos_relevantes(clean_all(query), k) # Recibe los documentos con su orden de relevancia
    palabras = clean_all(query) # Recibe un arrray de palabras ya limpias

    list_fined = search_valid(documentos , palabras)

    #print(len(list_fined[:k]))    
    return list_fined[:k]

#inverted = read_inverted()
#print(search_tweet("hola perras" , 1))
