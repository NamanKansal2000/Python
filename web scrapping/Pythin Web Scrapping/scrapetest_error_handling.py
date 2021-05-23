from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
# Url errors
try:
    html = urlopen("https://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return Null or break
except URLError as e:
    print("The server could not be found")
else:
    print("It worked")
