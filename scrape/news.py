__author__ = 'oski'

from lxml import html    #Use lxml library's html parser
from requests import get, put, post, delete   #Import commands from requests module
import io

##The function accepts a list of urls
def list_from_urls(urls):
    #Use requests to fetch url, then save to a file
    for url in urls:
        r = get(url)
        tree = html.fromstring(r.text)
        snippet = tree.xpath('//div[@class="snippet"]/text()')
        #print snippet
        fo = open("snippet.txt", "rw+")
        fo.write(snippet)
        fo.close()

test_urls = ['https://news.google.com/news?ncl=d8ovgjSMjdF1F-MYvjH0A6BKPiD0M&q=detroit&lr=English&hl=en&sa=X&ei=-mb2U_ydDtC7ogSvh4HwCg&ved=0CCYQqgIwAA']

list_from_urls(test_urls)

