import requests
import json
import time

# # 1. Setup credentials and target
# API_KEY = 'API-KEY'
# base_url = "https://newsapi.org/v2/everything"

# query_parameters = {
#     "q": "keyword", 
#     "apiKey": API_KEY,
#     "language": "en"
# }

# def process_or_store(data_item):
#     print(json.dumps(data_item, indent=2))

# # 3. Fetch the data from the internet
# print("Connecting to API and extracting text data...")
# response = requests.get(base_url, params=query_parameters)
# api_response_json = response.json()

# # 4. Loop, format, and process
# articles = api_response_json.get('articles', [])

# for article in articles[:10]:
#     formatted_item = {
#         "text": f"{article['title']}. {article['description']}",
#         "user_name": article['source']['name'],
#         "created_at": article['publishedAt']
#     }
    
#     process_or_store(formatted_item)


class NewsStreamer:
    def __init__(self, api_key, keyword):
        self.base_url = "https://newsapi.org/v2/everything"
        self.seen_articles = set()
        self.params = {
            "q": keyword,
            "apiKey": api_key,
            "language": "en",
            "sortBy": "publishedAt"
        }
    
    def on_data(self, article_data, filename):
        try:
            with open(filename, 'a') as f:
                f.write(json.dumps(article_data) + '\n')
            return True
        except BaseException as e:
            print(f"Error saving data: {str(e)}")
            return False

    def start_stream(self):
        print(f"Streaming news about {self.params['q']}... Press Ctrl + C to stop ")
        try:
            while True:
                response = requests.get(self.base_url, params=self.params)
                articles = response.json().get('articles', [])

                for article in articles:
                    title = article['title']
                    if title not in self.seen_articles:
                        self.seen_articles.add(title)

                        formatted_item = {
                            "text": f"{article['title']}. {article['description']}", 
                            "user_name": article['source']['name'],
                            "created_at": article['publishedAt']
                        }
                        self.on_data(formatted_item, 'python_news.json')

                time.sleep(15)
        except KeyboardInterrupt:
            print("\nStreaming stopped")

API_KEY = '07468e83e073454d88a1eb9f7646bcac'

streamer = NewsStreamer(api_key=API_KEY, keyword="python")
streamer.start_stream()

