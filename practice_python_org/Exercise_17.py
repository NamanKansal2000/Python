from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
for article in soup.find_all('article'):
    # print(article.prettify())
    try:
        headline = article.h2.a.text
        print('Title: ' + headline)
    except:
        print('Title: None')

    try:
        summary = article.find('div', class_='entry-content').p.text
        print('Summary: ' + summary)
    except:
        print('Summary: None')

    try:
        vid_src = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'http://www.youtube.com/watch/v={vid_id}'
        print('YouTube Link: ' + yt_link)
    except:
        print('YouTube Link: None')

    print()
