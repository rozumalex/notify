import feedparser
from pprint import pprint
from time import sleep
url = 'https://onliner.by/feed'

result = feedparser.parse(url)
for entry in result.entries:
    print(entry.title)
    print(entry.summary)
