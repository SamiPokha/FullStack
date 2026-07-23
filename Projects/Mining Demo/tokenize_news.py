import re
import json

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

print("Reading file and tokenizing items...\n")

# --- FILE LOOP ---
with open('python_news.json', 'r') as f:
    print(f"{'PUBLISHER':<20} | {'TOKENS EXTRACTED'}")
    print("-" * 70)
    
    for line in f:
        article = json.loads(line)
        raw_text = article['text']
        lowercased_text = raw_text.lower()
        tokens = tokenize(lowercased_text)
        
        publisher = article['user_name']
        # Show the first 8 real words extracted!
        print(f"{publisher:<20} | {tokens[:8]}")