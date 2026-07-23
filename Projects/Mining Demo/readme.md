# My Learning Process

## Part 1: Requests, APIs, and JSON Handling

### I. Getting Started with APIs
I have figured out how to use requests and API keys. Data is mostly stored in JSON format. The first steps are as follows:

*   Use the documentation of the RESTApi that you are using and find the API key and anything else that you need to use. Documentation will not have the API key, you need to get that yourself.
*   The starting will just be a few import statements, but make sure to add import json so that we can see the data in JSON format.
*   For this example, it was import requests, and we needed a URL that we need to personalize, such as:

```python
import json
import requests

url = f"[https://newsapi.org/v2/everything?q=crypto&apiKey=](https://newsapi.org/v2/everything?q=crypto&apiKey=){API_KEY}&language=en"
```

How the URL is broken down:
We can see that all the parameters are seperated by & from the main url https://newsapi.org/v2/everything which is shown in the documentation. The ? is the start of the parameters, and we just personalized it to have q (the keyword) as crypto and apiKey be our APIkey and etc.

---

### II. After Documentation
We need to actually get the data, which is simply done by the code `response = requests.get(url)` code, then we can get all of the articles by doing `all_articles = response.json().get('articles', [])`

Then if there are articles present, so the code `if all_articles`, then get the first article, `raw_article = all_articles[0]` then print the keys in a list using type casting `list(raw_article.keys())`

We can print the data by using `json.dumps()` and then inside we give the data that we want to display which in our case is raw_article and then we can have a second parameter indent=4 or 2, 8 for a cleaner display.

Code Implementation:
```python
response = requests.get(url)
all_articles = response.json().get('articles', [])

if all_articles:
    raw_article = all_articles[0]
    print(list(raw_article.keys()))
    print(json.dumps(raw_article, indent=4))
```

---

### III. Once We Understand Our Data
We do not want to manually change the url everytime, so we create query parameters, `query_parameters = {"q": keyword, "apiKey": API_KEY, "language": "en" }`, then in our `requests.get()` we add the base url and do `params=query_parameters`

```python
query_parameters = {"q": keyword, "apiKey": API_KEY, "language": "en"}
response = requests.get("[https://newsapi.org/v2/everything](https://newsapi.org/v2/everything)", params=query_parameters)
```

We can then, do `api_response = response.json()` and then use the get method on api_response with the parameter 'articles', [] to get an article, otherwise display an empty list.

Then we can loop through those and format it however we want, and then print it using `json.dumps(data_item, indent=4)`

```python
api_response = response.json()
articles = api_response.get('articles', [])

for data_item in articles:
    # Format it however we want
    print(json.dumps(data_item, indent=4))
```

---

### IV. The JSON Rules & Cheat Sheet
If you want to turn a Python dictionary into a JSON string (to save to a file or send away), use `json.dumps()`.

If you want to turn a JSON string coming from the web into a Python dictionary, use `response.json()`.

`json.loads()` is a general-purpose Python tool. It doesn't know anything about the internet or web requests; it just takes any raw string variable you hand it and converts it into a Python dictionary. Can be used after `line = f.readline`

| Scenario | What to use |
| :--- | :--- |
| From the internet directly? | Use `response.json()`. |
| From a text file or a local string variable? | Use `json.loads()`. |
| Going the opposite direction (Python Dict -> Text String)? | Use `json.dumps()` (Dump String) |

## Part 2: Text Pre-Processing and Tokenization

### I. Getting Started with Tokenization
I have figured out how to use regular expressions and tokenizers. Data is mostly broken down into a list of words. The first steps are as follows:

* Use the documentation of the regex rules that you are using and find the symbols and anything else that you need to use. Documentation will not have the exact array layout, you need to build that yourself.
* The starting will just be a few pattern setups, but make sure to add prefix r so that we can see the strings in a raw format.
* For this example, it was import re, and we needed an array list that we need to personalize, such as:

```python
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
```

How the layout order is broken down:
We can see that all the rules are checked from top to bottom by the main engine which is shown in the logic. The first rule is the start of the matching, and we just personalized it to have high-priority strings (the specific patterns) like HTML tags, Twitter mentions, hashtags, and URLs at the top, currencies and numbers in the middle, and standard word patterns or catch-all expressions at the bottom. This physical order matters because the engine stops searching the moment it satisfies any pattern; if a broad pattern sits above a specific one, it will steal the text and break complex terms like prices or links apart.

---

### II. After Configuration
We need to actually slice the data, which is simply done by the code `tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)` code, then we can get all of the tokens by doing `tokens = tokens_re.findall(s)` inside our function.

Then if there are tokens present, so the code `if search_keyword in tokens`, then lower case the original string, `article['text'].lower()` then filter the items in a list using the input match check.

We can view the clean data by using `print()` and then inside we give the data that we want to display which in our case is **article['user_name']** and **article['text']** and then we can have a separating string design `"-" * 60` for a cleaner display. This setup compiles our entire `regex_str` list into a single optimized pattern block by gluing them with a pipe symbol `|`, which tells the machine to check if it matches Rule 1 OR Rule 2 OR Rule 3.

Code Implementation:
```python
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE) 

def tokenize(s):
    return tokens_re.findall(s)

search_keyword = input("Enter a keyword to search for (e.g. bitcoin, openai, $): ").lower()
print("\nScanning your database...\n")
```

---

### III. Once We Understand Our Data
We do not want to manually write out regex compilation loops everytime, so we create a helper function, `def tokenize(s): return tokens_re.findall(s)`, then in our processing loop we pass the string and do `tokens = tokenize(article['text'].lower())`

```python
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
```

We can then, do `article = json.loads(line)` and then use the if method on tokens with the parameter `if search_keyword in tokens` to get an article match, otherwise display a no articles found print statement. This mapping allows us to build a reverse search filter where keywords are verified directly inside the isolated token array instead of forcing the computer to scan the full raw sentence text line character-by-character when searching.

Then we can loop through those and index it however we want, and then print it using formatting strings like `f"📝 Title: {article['text']}"`

---

### IV. The Regex Rules & Cheat Sheet
If you want to turn letters into a whole word block (gluing characters together), use `(?:[\w_]+)`. The `\w` matches any single letter or number, while the `+` acts as a multiplier saying "keep grabbing matching items as long as they appear next to each other."

If you want to pull strings from text that are not spaces (like individual punctuation marks), use `(?:\S)`. This is a capital letter rule that acts as a bottom fallback catcher to ensure standalone periods, commas, or weird symbols are preserved rather than thrown out by the engine.

`\` is a general-purpose regex tool. It doesn't know anything about alphanumeric characters on its own; it just takes any special symbol character you put behind it and disables its default engine power. Can be used before `$` so the system searches for a literal dollar sign in `(?:\$\d+(?:\.\d+)?)` instead of treating it as a command function.

## Part 3: Term Frequency and Counting

### I. Getting Started with Counting
I have figured out how to use collection counters and frequency trackers. Data is mostly calculated into a dictionary tally. The first steps are as follows:

* Use the documentation of the collections module that you are using and find the Counter class and anything else that you need to use. Documentation will not have your input data file, you need to provide that yourself.
* The starting will just be a few data tracking setups, but make sure to add from collections import Counter so that we can see the data in a summarized frequency format.
* For this example, it was import nltk, and we needed a file name that we need to personalize, such as:

```python
import json
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
import string

filename = 'python_news.json'
```

How the loop system is broken down:
We can see that all the lines are checked from top to bottom by the reader loop which is shown in the file execution. The first line is the start of the file processing, and we just personalized it to have a file stream open `with open(filename, 'r') as f:` at the top and counter metrics at the bottom. This layout tracking matters because the counter loops indefinitely until it consumes every single record inside the database; as lines fall through, it grabs the nested text key, passes it straight to our customized tokenizer engine, and streams the array fragments straight into our central tracker memory.

---

### II. After Configuration
We need to actually update the tally, which is simply done by the code `count = Counter()` code, then we can get all of the top frequencies by doing `count.most_common(5)` inside our print execution.

Then if there are articles present, so the code `for line in f`, then load the individual line object, `article = json.loads(line)` then extract the components in a list using list comprehension `[term for term in tokenize(article['text'].lower()) if term not in stop and len(term) > 1]`

We can view the frequency data by using `print()` and then inside we give the data that we want to display which in our case is **count_bigrams.most_common(5)** and then we can have a resulting frequency list display object `[(('python', 'sdk'), 24), (('added', 'pypi'), 18)]` for a cleaner display. This setup compiles our entire tokenized sentence streams into an active hash dictionary by running a `.update()` method, which tells the machine to check if the word pair is already tracked and instantly add a tally mark to its global score.

Code Implementation:
```python
nltk.download('stopwords')

# Stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['amp', 'news']

count = Counter()
count_bigrams = Counter()

with open(filename, 'r') as f:
    for line in f:
        article = json.loads(line)

        # Filter out short fragments and stop words dynamically
        terms = [term for term in tokenize(article['text'].lower()) 
                 if term not in stop and len(term) > 1]
        
        bigram_terms = list(bigrams(terms))
        
        count.update(terms)
        count_bigrams.update(bigram_terms)

print(count.most_common(5))
print(count_bigrams.most_common(5))
```

---

### III. Once We Understand Our Data
We do not want to blindly accept raw word counts everytime, so we create a filtering strategy, `list(bigrams(terms))`, then in our count extraction loop we chain adjacent terms together and do `count_bigrams.update(bigram_terms)`

```python
print(count_bigrams.most_common(5))
```

We can then, do `print(count_bigrams.most_common(5))` and then use the most_common method on count_bigrams with the parameter 5 to get a top score summary, otherwise display a messy list filled with loose disconnected vocabulary items. This final calculation allows us to see why phrase pairing matters because standard single tokens can eliminate semantic meaning whereas multi-word bigram fragments will isolate actual thematic actions like package additions or library wrappers instead of loose metadata flags.

Then we can look through those and analyze it however we want, and then see the layout output using a terminal list array like `[(('python', 'sdk'), 24), (('added', 'pypi'), 18)]`

---

### IV. The Counting Rules & Cheat Sheet
If you want to filter out tiny leftover single characters or loose artifact letters from your word sequence array, use `len(term) > 1`. This is an integer checking property condition that monitors string lengths to protect your calculations from micro noise values.

If you want to group your isolated vocabulary array into double-headed overlapping phrase pairs to discover contextual trends, use `bigrams()`. The engine operates like a moving window that links adjacent array tokens into standalone paired tuple objects.

`.most_common()` is a general-purpose calculation tool. It doesn't know anything about data importance or grammar rules on its own; it just takes any integer number parameter you put inside it and isolates that many high-ranking items from your dictionary. Can be used before printing or saving records.

| Scenario | What to use |
| :--- | :--- |
| Looking for the absolute highest frequency tokens in the dictionary? | Use `.most_common(N)`. The method isolates the top N champions sorted from greatest to least. |
| Merging an array of new tokens into your master scoreboard? | Use `.update()`. This adds values seamlessly without writing manual dictionary check loops. |
| Eliminating duplicate terms within an isolated document line to track item frequency? | Use `set(terms)`. This instantly collapses an array down to unique values. |

## Part 4: Term Co-Occurrences

### I. Getting Started with Co-Occurrences
I have figured out how to use nested dictionary grids and co-occurrence tracking systems. Data is mostly calculated into a structural cross-reference coordinate framework. The first steps are as follows:

* Use the documentation of the collections module that you are using and find the defaultdict class and anything else that you need to use. Documentation will not have your input data file, you need to provide that yourself.
* The starting will just be a few data tracking setups, but make sure to add from collections import defaultdict so that we can see the data in a summarized multi-dimensional coordinate format.
* For this example, it was import operator, and we needed a file name that we need to personalize, such as:

```python
import json
import re
import string
import operator
from collections import defaultdict

filename = 'python_news.json'
```

How the loop system is broken down:
We can see that all the lines are checked from top to bottom by the reader loop which is shown in the file execution. The first line is the start of the file processing, and we just personalized it to have a file stream open `with open(filename, 'r') as f:` at the top and nested tracking matrices at the bottom. This layout tracking matters because the matrix configuration loops indefinitely until it consumes every single record inside the database; as lines fall through, it grabs the nested text key, extracts our specific filtered keywords list, and maps row-by-column co-occurrence coordinate counts anywhere inside the document space.

---

### II. After Configuration
We need to actually update the matrix tally, which is simply done by the code `com = defaultdict(lambda: defaultdict(int))` code, then we can get all of the top frequencies by doing `sorted(com_max, key=operator.itemgetter(1), reverse=True)` inside our print execution.

Then if there are articles present, so the code `for line in f`, then load the individual line object, `article = json.loads(line)` then extract the components in a list using list comprehension `[term for term in tokenize(article['text'].lower()) if term not in stop and len(term) > 1 and not term.startswith(('@', '#'))]`

We can view the frequency data by using `print()` and then inside we give the data that we want to display which in our case is **terms[:5]** and then we can have a resulting frequency list display object `[(('python', 'sdk'), 80), (('added', 'pypi'), 65)]` for a cleaner display. This setup compiles our entire tokenized sentence streams into an active half-triangle coordinate hash grid by running a double-nested loop tracker, which tells the machine to alphabetize the paired strings and instantly add a tally mark to its global score row without wasting double the storage space.

Code Implementation:
```python
import re
import json
import string
import operator
from collections import defaultdict
from nltk.corpus import stopwords

# Ensure english stopwords are securely added to prevent structural noise
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

        # Isolate semantic context tokens by blocking tags, shorts, and stop words
        terms = [term for term in tokenize(article['text'].lower())
                 if term not in stop
                 and len(term) > 1
                 and not term.startswith(('@', '#'))
                 ]
        
        # Squeeze data loops to build a lean triangular matrix structure
        for i in range(len(terms) - 1):
            for j in range(i + 1, len(terms)):
                word1, word2 = sorted([terms[i], terms[j]])
                if word1 != word2:
                    com[word1][word2] += 1

# Flatten out the matrix rows to calculate high-ranking pairings globally
com_max = []
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))

terms = sorted(com_max, key=operator.itemgetter(1), reverse=True)

print("Top Occurrences:")
print(terms[:5])
```

---

### III. Once We Understand Our Data
We do not want to blindly accept raw word counts everytime, so we create a filtering strategy, `word1, word2 = sorted([terms[i], terms[j]])`, then in our count extraction loop we sort row elements and do `com[word1][word2] += 1`

```python
# Displays our clean keyword co-occurrences with sorted ranking parameters
print(terms[:5])
```

We can then, do `print(terms[:5])` and then use the slicing method on terms with the parameter 5 to get a top score summary, otherwise display a messy matrix filled with duplicated mirroring calculations. This final calculation allows us to see why structural coordinate matrix design matters because standard standalone word counts can lose context meanings whereas global co-occurrence algorithms will capture relational themes anywhere inside an article block.

Then we can look through those and analyze it however we want, and then see the layout output using a terminal list array like `[(('python', 'sdk'), 80), (('added', 'pypi'), 65), (('api', 'python'), 57)]`

---

### IV. The Counting Rules & Cheat Sheet
If you want to pull a conversion list of combined key-value tuple elements straight out of an isolated word row inside a tracking grid dictionary, use `.items()`. This method turns a dictionary row map into individual accessible pairs.

If you want to force the sorting calculation to prioritize the numeric frequency value at index 1 instead of sorting alphabetically by strings at index 0, use `operator.itemgetter(1)`. This functions as a precise numeric index pointer for the sorting backend.

`defaultdict()` is a general-purpose calculation tool. It doesn't know anything about data importance or grammar rules on its own; it just takes a lambda initialization condition parameter you put inside it and automatically builds missing nested dictionary entries. Can be used before printing or saving records.

| Scenario | What to use |
| :--- | :--- |
| Looking for the absolute highest frequency co-occurrences across the flattened database? | Use `sorted(com_max, key=operator.itemgetter(1), reverse=True)`. This organizes your data tuples by score value. |
| Initializing a nested grid dictionary to safely log data without running into crash keys? | Use `defaultdict(lambda: defaultdict(int))`. This sets default base values seamlessly. |
| Restricting data loop ranges to form a lean half-triangle shape that preserves memory limits? | Use `range(len(terms) - 1)` with `range(i + 1, len(terms))`. This bypasses duplicate backwards tracking. |

