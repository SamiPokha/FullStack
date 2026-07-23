import json
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
import string
import vincent

nltk.download('stopwords')

# Stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['amp', 'news']

regex_str = [
    r'<[^>]+>',
    r'(?:@[\w_]+)',
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:\$\d+(?:\.\d+)?)'
    r'\d+(?:\.[w\d]+)+'
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',
    r"(?:[a-z][a-z'\-_]+[a-z])",
    r'(?:[\w_]+)',
    r'(?:\S)'
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE) 

def tokenize(s):
    return tokens_re.findall(s)

filename = 'python_news.json'

count = Counter()
count_bigrams = Counter()

with open(filename, 'r') as f:
    for line in f:
        article = json.loads(line)

        terms = [term for term in tokenize(article['text'].lower()) 
                 if term not in stop and len(term) > 1]
        
        bigram_terms = list(bigrams(terms))
        count.update(terms)
        count_bigrams.update(bigram_terms)


word_freq = count.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('terms_freq.json')