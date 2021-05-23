from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://pythonscraping.com/pages/page1.html")
bsobj = BeautifulSoup(html.read(), 'lxml')
print(bsobj.h1)
print(bsobj.notExistentTag.sometag)
