import os

from src.clean import clean_all
import json
from collections import Counter
import math
from nltk.stem.snowball import SnowballStemmer
import nltk
nltk.download('punkt')

direction_dataset_clean = "./src/clean_data" 
nanmes_docs = os.listdir(direction_dataset_clean) 

direction_indexs = "./src/indexs/index"
ind = {}  




def read_inverted(): 
    print("readInverted():")    
    cont = 1
    
    while(True): 
        pat = direction_indexs + str(cont)+".txt"
        if os.path.exists(pat): 
            with open(pat, 'r', encoding="ISO-8859-1") as indice: 
                
                for line in enumerate(indice): 

                    pair = str(line[:len(line)-2]).split(':') 

                    if pair[0] in ind:
                        ind[pair[0]] = str(ind[pair[0]]) + ";" + str(pair[1]) 
                    else:
                        if len(pair) >= 2:
                            ind[pair[0]] = str(pair[1])
                        
            cont += 1
        else:
            break
    return ind


def get_frecuency(palabras): 
    stemmer = SnowballStemmer('spanish') 
    roots = [stemmer.stem(i) for i in palabras] 
    return Counter(roots) 


def documentos_relevantes(query): 
    
    tf = get_frecuency(query)
    dic = {} 
    
    inverted = read_inverted()
    
    scores = {}
    lenght1 = {}
    
    for i in nanmes_docs: 
        scores[i] = 0
        lenght1[i] = 0
    
    lenght2 = 0 
    
    for i in tf:
        
        print("tf[i]" , i)
        print("names_docs" , nanmes_docs)
        print("inverted[i]" , inverted[i])
        wtfidf = math.log(1 + tf[i]) * math.log(len(nanmes_docs) / len(inverted[i].split(';'))    ) 
        
        
        dic[i] = wtfidf

        lenght2 = lenght2 + wtfidf**2 

        values = inverted[i].split(';') 
        for j in values:  
            j = j.split(',') 
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
    print("search_tweet(query, k):")
    documentos = documentos_relevantes(clean_all(query)) 
    palabras = clean_all(query) 

    list_fined = search_valid(documentos , palabras)

    
    return list_fined[:k]



