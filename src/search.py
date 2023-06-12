import os
#from clean import clean_all
import json
from collections import Counter
import math
from nltk.stem.snowball import SnowballStemmer

direction_dataset_clean = "src\\clean_data" # Leemos del dataset ya limpio
nanmes_docs = os.listdir(direction_dataset_clean) #Obtener la lista de los nombres de los archivos del dataset limpio

direction_indexs = "indexs\\index"
ind = {}  



import nltk
import re


invalid_characters = [ "¡", "«", "»", ".", ",", ";", "(", ")", ":", "@", "RT", "#", "|", "¿", "?", "!", "https", "$", "%", "&", "'", "''", "..", "...", '\'', '\"' ] 

with open('dataset\\stoplist.txt') as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += invalid_characters



# Limpieza
def signosp(word): # Eliminar los signos de puntuación de una palabra y devuelve la palabra sin los signos
    for x in word:
        if x in invalid_characters:
            word = word.replace(x, "")
    return word

# Limpieza
def remove_URL(sample):
    return re.sub(r"http\S+", "", sample)

# Limpieza
def remove_emoji(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"\\u\S+", "", sample)

# Limpieza
""" def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text """
def give_emoji_free_text(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u200b"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               u"\u2066"
                               u"\u2069"
                               u"\u0144"
                               u"\u0148"
                               u"\u2192"
                               u"\u2105"
                               u"\u02dd"
                               u"\u0123"
                               u"\u0111"
                               u"\u013a"
                               u"\u2193"
                               u"\u2191"
                               u"\u0307"
                               u"\u0435"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


# Limpieza
""" def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u200b"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        u"\u2066"
        u"\u2069"
        u"\u0144"
        u"\u0148"
        u"\u2192"
        u"\u2105"
        u"\u02dd"
        u"\u0123"
        u"\u0111"
        u"\u013a"
        u"\u2193"
        u"\u2191"
        u"\u0307"
        u"\u0435"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)
 """
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u200b"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        u"\u2066"
        u"\u2069"
        u"\u0144"
        u"\u0148"
        u"\u2192"
        u"\u2105"
        u"\u02dd"
        u"\u0123"
        u"\u0111"
        u"\u013a"
        u"\u2193"
        u"\u2191"
        u"\u0307"
        u"\u0435"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


# Limpieza
""" def strip_emoji(text):
    new_text = re.sub(emoji.get_emoji_regexp(), r"", text)
    return new_text
 """
def strip_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u200b"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               u"\u2066"
                               u"\u2069"
                               u"\u0144"
                               u"\u0148"
                               u"\u2192"
                               u"\u2105"
                               u"\u02dd"
                               u"\u0123"
                               u"\u0111"
                               u"\u013a"
                               u"\u2193"
                               u"\u2191"
                               u"\u0307"
                               u"\u0435"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def clean_all(text):
    ans = []
    palabras = nltk.word_tokenize(remove_URL(signosp(strip_emoji(remove_emojis(text))).lower()))
    for token in palabras:
        if token not in stoplist:
            ans.append(token)
    return ans


# Busqueda
def parser(line):
    i = line.split(':')
    return i


# Busqueda
def df_ind(word, ind):
    line = ind[word]
    line = line.split(';')
    return len(line)

# Busqueda
def readInverted(): #Lee los indices, y retorna un diccionario de indices(Ya une con todos los archivos)
    print("readInverted():")
    
    cont = 1
    
    
    while(True): # Lee los indices invertidos
        pat = direction_indexs + str(cont)+".txt"
        if os.path.exists(pat): # Mientras existe el archivo
            with open(pat, 'r', encoding="ISO-8859-1") as f: # Abre el archivo
                #print("leyendo indices: " , f)
                for index, line in enumerate(f):  # Leemos de forma enumerada lo del archivo abierto
                    pair = parser(line[:len(line)-2])
                    if pair[0] in ind:
                        ind[pair[0]] = str(ind[pair[0]]) + ";" + str(pair[1]) #Si es que ya existe, concatenamos al anterior   
                    else:
                        ind[pair[0]] = str(pair[1]) # Si no existe crea uno nuevo
            cont += 1
        else:
            break
    return ind

# Busqueda
def get_frecuency(name): # Hace limpieza, filtra palabras clave, retrona frecuencias
    stemmer = SnowballStemmer('spanish') # Cojemos las palabras clave
    palabras = clean_all(name)
    roots = [stemmer.stem(i) for i in palabras] # Convertimos todas las palbras en su base raiz
    return Counter(roots) # Cuenta la frecuencia de cada palabra (devuelve en diccionario)

# Busqueda
def documentos_relevantes(query, k): # Retorna una lista ordenada de los documentos mas relevantes en una consulta (query)
    tf = get_frecuency(query) # Palabras con sus frecuencias (Diccionario )
    dic = {} 
    
    inverted = readInverted()# Indices, palabras y documentos (Diccionario)
    scores = {}
    lenght1 = {}
    # aseguramos que los puntajes y las longitudes se inicien en 0 antes de calcularlos 
    for i in nanmes_docs: # Recorremos los nombres de los archivos limpios
        scores[i] = 0
        lenght1[i] = 0
    
    lenght2 = 0 #Para calcular la suma de los cuadrados de los pesos
    #REcorremos las palabras con sus frecuencias
    for i in tf:
        # math.log(1 + tf[i]): Aplica una transformación logarítmica a la frecuencia del término en el documento. El 1 es para evitar tomar el logaritmo de cero en caso de que el término no aparezca en el documento.
        # math.log(len(archivos)/df_ind(i, inverted)) : Calcula la frecuencia inversa del termino , para reducir la importancia del termino que aparecen en muchos documentos
         
        wtfidf = math.log(1 + tf[i]) * math.log(len(nanmes_docs)/df_ind(i, inverted)) # Representa al peso: tf-idf
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
    #return orderedDic[:k]


# Busqueda
def search_tweet(query, k): # Retorna los tweets encontrados
    print("search_tweet(query, k):")
    documentos = documentos_relevantes(query, k) # Recibe los documentos con su orden de relevancia
    palabras = clean_all(query) # Recibe un arrray de palabras ya limpias
    
    
    #print(documentos)
    #print(palabras)
    
    """
    - leer los documentos con su orden de relevancia, leemos los documentos , 
    recorremos las palabras a buscar limpias, 
    """
    
    lista = []
    
    for i in documentos:
        with open(direction_dataset_clean + '\\' + i[0], 'r', encoding='utf-8' ) as documentos_encontrados:
            relevantes_cargados= json.load(documentos_encontrados)
            for letter in palabras: # Query
                for twet in relevantes_cargados:
                    temp = relevantes_cargados[twet]
                    if temp.find(letter) != -1: # Retorna -1 si no lo encuentra
                        lista.append( {twet , relevantes_cargados[twet] })# Agregamos el tweet con su valor
                        #lista.append( {twet})
                    
    
    print("Lista encontrada")
    #print(len(lista[:k]))    
    return lista[:k]


print(search_tweet("hola perras" , 1))
