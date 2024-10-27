import numpy as np
import nltk
import unicodedata
from nltk.stem.porter import PorterStemmer
 
stemmer = PorterStemmer()

def tokenize(sentence):
   
    return nltk.word_tokenize(sentence)

def stem(word):

    return stemmer.stem(word.lower())

def normalize_text(text):
   
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    return text

def bag_of_words(tokenized_sentence, words):

    
    sentence_words = [stem(normalize_text(word)) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag
