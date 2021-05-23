import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
product_url = 'https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=26653404'
response = requests.get(product_url, headers=headers)
soup = response.json()

json_val = soup['navData']

count = 0
ls = []
print(json_val.keys())
for k in json_val.keys():

    val = json_val[k]['tabs'][0]['columns']
    for i in range(len(val)):
        for j in range(len(val[i])):
            count += 1
            title = val[i][j]['title']
            try:
                url = 'www.flipkart.com' + val[i][j]['url']
            except:
                url = ''
            try:
                type = val[i][j]['type']
            except:
                type = ''
            print(url)
            write = title + ',' + url + ',' + type + '\n'

            # print(write)


with open('navBar_links.txt', 'w') as fh:
    for val in ls:
        fh.write(val)
