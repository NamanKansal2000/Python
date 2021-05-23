import requests
from bs4 import BeautifulSoup
import json

ls = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
for i in range(1, 51):
    product_url = 'https://www.flipkart.com/search?q=electronics&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}'.format(
        i)
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    all_class = soup.find_all('div', {'class': '_3liAhj'})
    for val in all_class:
        try:
            title = val.find('a', {'class': '_2cLu-l'}).text.strip()
        except:
            title = ''
        try:
            url = 'https://www.flipkart.com'+val.a['href']
        except:
            url = ''
        try:
            no_of_reviews = val.find('span', {'class': '_38sUEc'}).text.strip()[1:-1]
        except:
            no_of_reviews = ''
        try:
            price = val.find('div', {'class': '_1vC4OE'}).text.strip()[1:]
        except:
            price = ''
        try:
            reviews = val.find('div', {'class': 'hGSR34'}).text.strip()
        except:
            reviews = ''
        try:
            discount = val.find('div', {'class': 'VGWI6T'}).text.strip()
        except:
            discount = ''
        str_ = title + '|' + url + '|' + no_of_reviews + '|' + price + '|' + reviews + '|' + discount + '\n'
        ls.append(str_)
        print(str_)
    print(len(all_class))


with open('flipkart_elec.txt', 'w'):
    for val in ls:
        f.write(val)
