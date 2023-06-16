import nltk
import re
import string

stop_list_direction = './src/dataset/stoplist.txt'


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

""" def strip_emoji(text):
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

 """

def clean_all(text):
    ans = []
    palabras = nltk.word_tokenize(remove_URL(remove_signes(remove_emojis(text))).lower())
    for token in palabras:
        if token not in stoplist:
            ans.append(token)
    return ans


with open(stop_list_direction) as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += invalid_characters

