__author__ = 'oski'


from lxml import html    #Use lxml library's html parser
from requests import get, put, post, delete   #Import commands from requests module
import io

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

