import re
import json

regex_str = [
    r'<[^>]+>',
    r'(?:@[\w_]+)',
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:\$\d+(?:\.\d+)?)', 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  
    r"(?:[a-z][a-z'\-_]+[a-z])",   
    r'(?:[\w_]+)',                 
    r'(?:\S)'                      
]
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE) 

def tokenize(s):
    return tokens_re.findall(s)

search_keyword = input("Enter a keyword to search for (e.g. bitcoin, openai, $): ").lower()
print("\nScanning your database...\n")

matches_found = 0

with open('python_news.json', 'r') as f:
    for line in f:
        article = json.loads(line)
        
        # 1. Tokenize the text properties
        tokens = tokenize(article['text'].lower())
        
        # 2. Check if the user's exact keyword token is in the list!
        if search_keyword in tokens:
            matches_found += 1
            print(f"Match #{matches_found} found!")
            print(f"Source: {article['user_name']}")
            print(f"Title: {article['text']}")
            print("-" * 60)

if matches_found == 0:
    print(f"No articles found containing the keyword token '{search_keyword}'.")