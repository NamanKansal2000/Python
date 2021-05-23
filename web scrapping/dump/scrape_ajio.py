import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

base_url = "https://www.ajio.com/women/c/8303?query=:relevance"
r = requests.get(base_url, headers=headers)
# print(r.content)
soup = BeautifulSoup(r.content, 'lxml')

scripts = soup.find_all("div", {"class": "items"})[81]

print(val)
print()
# print(scripts[11])
# script = scripts.split('=')
# script = script.rstrip()
# script = script[:-1]
#
# data = json.loads(script)

# skus = list(data['grid']['entities'].keys())
#
# prodpage = []
# for sku in skus:
#     prodpage.append('https://www.ajio.com{}'.format(data['grid']['entities'][sku]['url']))
#
# print(len(prodpage))
