
__author__ = 'pangolin'

from lxml import html    #Use lxml library's html parser
#import requests         #Use requests module
from requests import get, put, post, delete   #Import commands from requests module
import io     #Use this to fix encoding


##An example
# r = get('http://statsforchange.org') #Get the data
# print 'status', r.status_code        #See httpstatus.es for codes
# print 'initial text:', r.text[:40]   #See some of the data
# tree = html.fromstring(r.text)   #Make a tree from the data
# print tree.body.text_content()   #See text content from the tree

##The function accepts a list of urls
def save_web_to_file(urls):
    '''Use requests to fetch url, then save to a file '''
    for url in urls:
        r = get(url)
        stripped_url = url.split('//')[1]
        filename = stripped_url.replace('/','_')
        with io.open(filename, 'w', encoding='utf8') as outfile:  #Open a new file and write to it
            outfile.write(r.text)

#A single page
test_url = ['http://statsforchange.org']

#Multiple pages
test_urls = [test_url, 'http://sfbay.craigslist.org/mca/']

#save_web_to_file(test_url)
save_web_to_file(test_urls)



