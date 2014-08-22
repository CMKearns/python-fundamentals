#Web scraping functions

__author__ = 'oski'


from lxml import html    #Use lxml library's html parser
from requests import get, put, post, delete   #Import commands from requests module
import io
import csv

##The function accepts a list of urls
def save_web_to_file(urls):
    #Use requests to fetch url, then save to a file
    for url in urls:
        r = get(url)
        stripped_url = url.split('//')[1]
        filename = stripped_url.replace('/', '_')[:50]
        with io.open(filename, 'w', encoding='utf8') as outfile:
            #Open a new file and write to it
            outfile.write(r.text)

##The function accepts a list of urls
def craigslist_table(urls):
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
        #Write to csv
        stripped_url = url.split('//')[1]
        filename = stripped_url.replace('/', '_')[:25]+'_table.csv'
        with open(filename, "w") as output:
            writer = csv.writer(output,lineterminator='\n')
            writer.writerows(table)



