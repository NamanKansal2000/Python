import requests
from bs4 import BeautifulSoup
import json

with open('amazon_smartphone.txt', 'w', encoding='utf-8') as f:
    for j in range(1, 401):
        # j = 200
        print(f'Getting page {j}')
        url = 'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031&page={}&qid=1601375083&ref=lp_1389401031_pg_{}'.format(
            j, j)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        html = requests.get(url, headers=headers)
        bsobj = BeautifulSoup(html.content, 'lxml')
        all_class = bsobj.find_all('div', {
            'data-component-type': 's-search-result'})
        all_class = all_class[1:]
        for val in all_class:
            try:
                title = val.h2.text.strip()
            except:
                title = ''
            try:
                rating = val.find('span', {'class': 'a-icon-alt'}).text.strip()
            except:
                rating = ''
            try:
                price = val.find('span', {'class': 'a-price-whole'}).text.strip()
            except:
                price = ''
            # try:
            #     actual_price = val.find('span', {'class': 'a-price a-text-price'}).text.strip()
            # except:
            #     actual_price = ''
            # print(title)
            # print(rating)
            print(price)
            # print(actual_price)
            str = title + '|' + rating + '|' + price + '\n'
            f.write(str)

        print(len(all_class))
