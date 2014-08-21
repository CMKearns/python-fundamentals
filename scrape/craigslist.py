#In chrome, see "Inspect Element" for html code

__author__ = 'oski'

from lxml import html    #Use lxml library's html parser
from requests import get, put, post, delete   #Import commands from requests module
import io

##The function accepts a list of urls
def list_from_urls(urls):
    for url in urls:
        r = get(url)
        tree = html.fromstring(r.text)
        entries = tree.xpath('//span[@class="txt"]')
        table = []
        for e in entries:
            print e.text_content()
            #Each element is a list, so take the first (and only) entry
            #Use try - except to avoid indexing errors
            try:
                price = e.xpath('.//span[@class="price"]/text()')[0]
                date = e.xpath('.//span[@class="date"]/text()')[0]
            except IndexError:
                continue
            table.append([date,price])
        print table

test_urls = ['http://sfbay.craigslist.org/mca/']

list_from_urls(test_urls)

