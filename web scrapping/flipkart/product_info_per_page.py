import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
product_url = 'https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts'
response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify().encode())
cont = soup.find_all('div', {'class': '_1HmYoV _35HD7C'})[
    1].find_all('div', {'class': 'bhgxx2 col-12-12'})
print(len(cont))

pages = cont[-2].find('div', {'class': '_2zg3yZ'}).span.get_text().split()[-1]
print(pages)
