import requests
from pprint import pprint

url = 'https://twitter.com/interpol_hq'
url = 'https://onliner.by/feed'

response = requests.get(url)
pprint(response.text)