import nltk
import re
import string
import os
from collections import Counter
from nltk.stem.snowball import SnowballStemmer
stop_list_direction = 'dataset\\stoplist.txt'
#stop_list_direction = './src/dataset/stoplist.txt'


invalid_characters = [ "¡", "«", "»", ".", ",", ";", "(", ")", ":", "@", "RT", "#", "|", "¿", "?", "!", "https", "$", "%", "&", "'", "''", "..", "...", '\'', '\"' ] 


def remove_signes(word):
    translator = str.maketrans("", "", string.punctuation)
    return word.translate(translator)


def remove_URL(sample):
    return re.sub(r"http\S+", "", sample)



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

def clean_all(text):
    ans = []
    
    palabras = nltk.word_tokenize(remove_URL(remove_signes(remove_emojis(text))).lower())
    for token in palabras:
        if token not in stoplist:
            ans.append(token)
    return ans

# def clean_all2(text):
#     ans = []
    
#     palabras = nltk.word_tokenize(remove_URL(remove_signes(remove_emojis(text))).lower())
#     for token in palabras:
#         if token not in stoplist:
#             ans.append(token)
#     return ans

def clean_all2(name): # Hace limpieza, filtra palabras clave, retrona frecuencias
    ans = []
    stemmer = SnowballStemmer('spanish') # Cojemos las palabras clave
    palabras = nltk.word_tokenize(remove_URL(remove_signes(remove_emojis(name)).lower()))
    for token in palabras:
        word = stemmer.stem(token) # Cada palabra en su base raiz
        if word not in stoplist: # que la palabra no se encuenre en la lista de los stoplisty
            ans.append(word)
    return Counter(ans) # Cuenta la frecuencia de cada palabra (devuelve en diccionario)

with open(stop_list_direction) as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += invalid_characters

