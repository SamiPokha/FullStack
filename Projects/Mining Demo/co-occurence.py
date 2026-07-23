import re
import json
import string
import operator
import nltk
from collections import defaultdict
from nltk.corpus import stopwords

nltk.download('stopwords')

punctuation = list(string.punctuation) + ['...', '’', '‘']
stop = stopwords.words('english') + ["news", "amp"] + punctuation

regex_str = [
    r'<[^>]+>',
    r'(?:@[\w_]+)',
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:\$\d+(?:\.\d+)?)',
    r"(?:[a-z][a-z'\-_]+[a-z])",
    r'(?:[\w_]+)',
    r'(?:\S)'
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

def tokenize(text):
    return tokens_re.findall(text)

filename = 'python_news.json'

com = defaultdict(lambda: defaultdict(int))

with open(filename, 'r') as f:

    for line in f:
        article = json.loads(line)

        terms = [term for term in tokenize(article['text'].lower())
                 if term not in stop
                 and len(term) > 1
                 and not term.startswith(('@', '#'))
                 ]
        
        for i in range(len(terms) - 1):
            for j in range(i + 1, len(terms)):
                word1, word2 = sorted([terms[i], terms[j]])
                if word1 != word2:
                    com[word1][word2] += 1

com_max = []
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))

terms = sorted(com_max, key=operator.itemgetter(1), reverse=True)

print("Top Occurences:")
print(terms[:5])

