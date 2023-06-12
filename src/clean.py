import nltk
import re


invalid_characters = [ "¡", "«", "»", ".", ",", ";", "(", ")", ":", "@", "RT", "#", "|", "¿", "?", "!", "https", "$", "%", "&", "'", "''", "..", "...", '\'', '\"' ] 

with open('.src/dataset/stoplist.txt') as file:
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
