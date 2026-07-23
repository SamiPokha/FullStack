import requests
import json

API_KEY = '07468e83e073454d88a1eb9f7646bcac'
url = f"https://newsapi.org/v2/everything?q=crypto&apiKey={API_KEY}&language=en"

response = requests.get(url)
all_articles = response.json().get('articles', [])

if all_articles:
    # 1. Grab the absolute first raw article
    raw_article = all_articles[0]
    
    print("--- Available Attributes (Keys) ---")
    print(list(raw_article.keys()))
    
    print("\n--- Full Raw Article Object ---")
    print(json.dumps(raw_article, indent=4))