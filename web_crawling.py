import requests
from bs4 import BeautifulSoup

def spider(max_pages):   # max pages to crawl through
    page = 1
    while page <= max_pages:
        url = 'https://en.wikipedia.org/wiki/Hello'      #url to crawl
        source_code = requests.get(url)     #to gather the source code of the web page to crwal through
        plain_text = source_code.text       # it removes all the crap like headers and all from source_code and stores
                                            # only texts and images, rather the good stuff
        soup = BeautifulSoup(plain_text)        # this variable gathers all the specific stuff in soure code that is required

        for line in soup.findAll('a', {'class':'mw-disambig'}):     #this finds all the class name of the given titles we need to crawl through
                                                           #"mw-disambig" is the class name to crawl through to find the titles in the webpage
            href = link.get('href')         # it gathers 'href'/url from the source code of "only" the title
            print(href)
        page += 1

spider(1)




