import os

from src.clean import clean_all, clean_all2
import json
from collections import Counter
import math
from nltk.stem.snowball import SnowballStemmer
import nltk
nltk.download('punkt')

direction_dataset_clean = "./src/clean_data" 


direction_indexs = "./src/indexs/index"
ind = {}  




def read_inverted(): 
    
    cont = 1
    print("direccion del indice: " ,direction_indexs )
    while(True): 
        pat = direction_indexs + str(cont)+".txt"
        #print("leyendo de:" , pat)
        if os.path.exists(pat): 
            with open(pat, 'r', encoding="ISO-8859-1") as indice: 
                
                for index , line in enumerate(indice): 
                    
                    pair = line[:len(line)-2].split(':')

                    if pair[0] in ind:
                        ind[pair[0]] = str(ind[pair[0]]) + ";" + str(pair[1]) 
                    else:
                        if len(pair) >= 2:
                            ind[pair[0]] = str(pair[1])
                        
            cont += 1
        else:
            break
    #print("indice invertido leido" , ind)
    return ind


def get_frecuency(palabras): 
    stemmer = SnowballStemmer('spanish') 
    roots = [stemmer.stem(i) for i in palabras] 
    return Counter(roots) 


""" def documentos_relevantes(query): 
    #print("DOCUMENTO RELEVANTES: " ,direction_dataset_clean )
    nanmes_docs = os.listdir(direction_dataset_clean) 
    print("nanmes_docs" , nanmes_docs)
    tf = get_frecuency(query)
    #print("fercuencia query," , tf)
    dic = {} 
    
    inverted = read_inverted()
    
    scores = {}
    lenght1 = {}
    
    for i in nanmes_docs: 
        scores[i] = 0
        lenght1[i] = 0
    
    lenght2 = 0 
    print("aqui1")
    for i in tf:
        wtfidf = math.log(1 + tf[i]) * math.log(len(nanmes_docs) / len(str(inverted[i]).split(';')))   
        print("----")
        
        dic[i] = wtfidf

        lenght2 = lenght2 + wtfidf**2 

        values = inverted[i].split(';') 
        for j in values:  
            j = j.split(',') 
            lenght1[j[0]] = lenght1[j[0]] + float(j[1])**2
            scores[j[0]] = scores[j[0]] + float(j[1])*wtfidf
    

    lenght2 = lenght2**0.5
    #Normalizacion de los puntajes de relevancia
    for i in lenght1:
        if lenght1[i] != 0:
            lenght1[i] = lenght1[i]**0.5
    for i in scores:
        if lenght1[i] != 0:
            scores[i] = scores[i]/(lenght1[i]*lenght2)
    print("aqui2")
    orderedDic = sorted(scores.items(), key=lambda it: it[1], reverse=True)
    print(orderedDic)
    return orderedDic """
def obtener_nombres_documentos():
    return os.listdir(direction_dataset_clean)

def calcular_tf(query):
    return get_frecuency(query)

def calcular_wtfidf(tf, inverted, document_count):
    wtfidf_scores = {}
    lenght2 = 0

    for term, frequency in tf.items():
        wtfidf = math.log(1 + frequency) * math.log(document_count / len(str(inverted[term]).split(';')))
        wtfidf_scores[term] = wtfidf
        lenght2 += wtfidf ** 2

    return wtfidf_scores, lenght2

def actualizar_puntajes(scores, lenght1, inverted, wtfidf_scores):
    for term, wtfidf in wtfidf_scores.items():
        values = inverted[term].split(';')
        for value in values:
            document_id, frequency = value.split(',')
            lenght1[document_id] += float(frequency) ** 2
            scores[document_id] += float(frequency) * wtfidf

    return scores, lenght1

def normalizar_puntajes(scores, lenght1, lenght2):
    for document_id in lenght1:
        if lenght1[document_id] != 0:
            lenght1[document_id] = lenght1[document_id] ** 0.5

    for document_id in scores:
        if lenght1[document_id] != 0:
            scores[document_id] = scores[document_id] / (lenght1[document_id] * lenght2)

    return scores

def documentos_relevantes(query):
    nombres_docs = obtener_nombres_documentos()
    print("nombres_docs", nombres_docs)

    tf = calcular_tf(query)
    inverted = read_inverted()

    scores = {}
    lenght1 = {}

    for document_id in nombres_docs:
        scores[document_id] = 0
        lenght1[document_id] = 0

    wtfidf_scores, lenght2 = calcular_wtfidf(tf, inverted, len(nombres_docs))
    scores, lenght1 = actualizar_puntajes(scores, lenght1, inverted, wtfidf_scores)
    scores = normalizar_puntajes(scores, lenght1, lenght2)

    print("aqui2")
    orderedDic = sorted(scores.items(), key=lambda it: it[1], reverse=True)
    print(orderedDic)
    return orderedDic




def search_valid(documentos , palabras):        
    """
    - leer los documentos con su orden de relevancia, leemos los documentos , 
    recorremos las palabras a buscar limpias, 
    """    
    lista = []        
    for i in documentos:
        with open(direction_dataset_clean + '/' + i[0], 'r', encoding='utf-8' ) as documentos_encontrados:
            relevantes_cargados= json.load(documentos_encontrados)
            for letter in palabras: 
                for twet in relevantes_cargados:
                    temp = relevantes_cargados[twet]
                    if temp.find(letter) != -1: 
                        lista.append( {twet , relevantes_cargados[twet] })
                        
    return lista
                    

def search_tweet(query, k): 
    print("search_tweet_local(query, k):")
    global direction_dataset_clean
    direction_dataset_clean = "./src/clean_data" 

    global direction_indexs
    direction_indexs =  "./src/indexs-local/index"
    documentos = documentos_relevantes(clean_all(query)) 
    palabras = clean_all(query) 

    list_fined = search_valid(documentos , palabras)

    
    return list_fined[:k]




def search_tweet_web(query, k): 
    global direction_dataset_clean
    direction_dataset_clean = "./src/clean_data_dev"

    global direction_indexs
    direction_indexs = "./src/indexs-web/index"
    print("search_tweet_web(query, k):")
    documentos = documentos_relevantes(clean_all(query)) 
    print("DOCUMENTOS" , documentos)
    palabras = clean_all(query) 
    print("PALABRAS" , documentos)
    list_fined = search_valid(documentos , palabras)

    
    return list_fined[:k]
