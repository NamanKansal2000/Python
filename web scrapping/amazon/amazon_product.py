import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
product_url = 'https://www.amazon.in/Nokia-105-2019-Single-Black/dp/B07YYNX5X6/ref=sr_1_35?dchild=1&qid=1598372388&s=electronics&sr=1-35'
response = requests.get(product_url, headers=headers)
# print(response.text)
top = 'product_name' + "," + 'category' + "," + 'product_features' + "," + 'product_price' + "," + \
    'price_was' + "," + 'review_count' + "," + 'rating' + "," + 'product_specifications' + "\n"
soup = BeautifulSoup(response.content, features="lxml")
try:
    title = soup.find('h1', {'id': "title"}).get_text().strip()
    # print(title)
except:
    title = 'NA'
categories = []
try:
    for li in soup.select("#wayfinding-breadcrumbs_container ul.a-unordered-list")[0].findAll("li"):
        categories.append(li.get_text().strip())
    categories = '**'.join(categories)
except:
    categories = 'NA'

features = []
try:
    for li in soup.select("#feature-bullets ul.a-unordered-list")[0].findAll('li'):
        features.append(li.get_text().strip())
    features = '**'.join(features)
except:
    features = 'NA'

try:
    price = str(soup.find("span", {'id': 'priceblock_ourprice'}).get_text())
except:
    price = 'NA'

try:
    price_was = str(
        soup.find("span", {'class': 'priceBlockStrikePriceString a-text-strike'}).get_text())
except:
    price_was = 'NA'

try:
    review_count = str(soup.select("#acrCustomerReviewText")[0].get_text().split()[0])
except:
    review_count = 'NA'

try:
    rating = soup.find("span", {'class': 'a-icon-alt'}).get_text()
except:
    rating = 'NA'

product_info = {}
try:
    table = soup.find('div', {'id': 'productDetails_feature_div'}).find(
        "table", {'id': 'productDetails_techSpec_section_1'}).find_all('tr')

    # print(table)
    for val in table:
        product_info[val.th.get_text().strip()] = val.td.get_text().strip()
    product_info = json.dumps(product_info, indent=2)
except:
    product_info = 'NA'


line = title + "," + categories + "," + features + "," + price + "," + \
    price_was + "," + review_count + "," + rating + "," + product_info + "\n"
print(line)
