import json

with open('crypto_news.json') as f:
    line = f.readline()
    article = json.loads(line)
    print(json.dumps(article, indent=4))