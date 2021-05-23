import requests
from bs4 import BeautifulSoup
import json
import re


def get_source(page_num=1):
    url = 'https://www.ajio.com/api/category/830216001?fields=SITE&currentPage={}&pageSize=45&format=json&query=%3Arelevance%3Abrickpattern%3AWashed&sortBy=relevance&gridColumns=3&facets=brickpattern%3AWashed&advfilter=true'

    res = requests.get(url.format(1), headers={'User-Agent': 'Mozilla/5.0'})
    if res.status_code == 200:
        return res.json()


# data = get_source(page_num = 1)
# total_pages = data['pagination']['totalPages'] # total pages are 111
prodpage = []
for i in range(1, 112):
    print(f'Getting page {i}')
    data = get_source(page_num=i)['products']
    for item in data:
        prodpage.append('https://www.ajio.com{}'.format(item['url']))
    if i == 3:
        break
print(len(prodpage))  # output 135 for 3 pages
