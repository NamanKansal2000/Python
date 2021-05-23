import requests
from bs4 import BeautifulSoup
import json

with open('amazon_elec.txt', 'w', encoding='utf-8') as f:
    for j in range(1, 401):
        print(f'Getting page {j}')
        url = "https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031&page=" + \
            str(j)+"&qid=1598372388&ref=lp_1389401031_pg_"+str(j)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        html = requests.get(url, headers=headers)
        bsobj = BeautifulSoup(html.content, 'lxml')

        # print(all_class[1].prettify())
        all_class = bsobj.find_all('div', {
            'data-component-type': 's-search-result'})

        for cont in all_class:
            print('*********')
            div = cont.h2.find('a', {'class': 'a-link-normal a-text-normal'}, href=True)
            product_url = 'https://www.amazon.in' + div['href']

            # scraping data

            response = requests.get(product_url, headers=headers)
            # print(response.text)
            top = 'product_name' + "," + 'category' + "," + 'product_features' + "," + 'product_price' + "," + \
                'price_was' + "," + 'review_count' + "," + 'rating' + "," + 'product_specifications' + "\n"
            f.write(top)
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
            f.write(line)
            print('*********')
