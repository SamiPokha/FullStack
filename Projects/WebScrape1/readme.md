# Scrapy

## Scrapy as an automated factory assembly line

1. **The Spider** is the worker who goes to a website address, downloads the raw web page, and brings it back to the factory.
2. **The Selector (Tweezers)** is the tool used to pick out specific pieces of data (title, price) from that raw web page. 
3. **The Item (Standard Box)** is a clean, labeled container where you drop those picked pieces of data so everything stays organized. 
4. **The Pipeline (Warehouse)** takes those filled boxes and saves them into a file or database like mongoDB.