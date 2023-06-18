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
    for i in lenght1:
        if lenght1[i] != 0:
            lenght1[i] = lenght1[i]**0.5
    for i in scores:
        if lenght1[i] != 0:
            scores[i] = scores[i]/(lenght1[i]*lenght2)
    print("aqui2")
    orderedDic = sorted(scores.items(), key=lambda it: it[1], reverse=True)
    print(orderedDic)
    return orderedDic
 """
def documentos_relevantes(query):
    documentos = os.listdir(direction_dataset_clean)
    tf = get_frecuency(query)
    inverted = read_inverted()
    
    scores = {}
    document_lengths = {}
    
    for documento in documentos:
        scores[documento] = 0
        document_lengths[documento] = 0
    
    for term, term_frequency in tf.items():
        if term not in inverted:
            continue
        
        idf = math.log(len(documentos) / len(inverted[term].split(';')))
        wtfidf = math.log(1 + term_frequency) * idf
        
        for doc_term in inverted[term].split(';'):
            document_id, doc_frequency = doc_term.split(',')
            document_id = int(document_id)
            doc_frequency = float(doc_frequency)
            
            document_lengths[document_id] += doc_frequency ** 2
            scores[document_id] += doc_frequency * wtfidf
    
    query_length_sqrt = math.sqrt(sum(tfidf ** 2 for tfidf in scores.values()))
    
    ordered_documents = []
    for document_id, score in scores.items():
        if document_lengths[document_id] != 0:
            score /= (math.sqrt(document_lengths[document_id]) * query_length_sqrt)
        ordered_documents.append({'document_id': document_id, 'score': score})
    
    ordered_documents.sort(key=lambda item: item['score'], reverse=True)
    
    return ordered_documents


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
