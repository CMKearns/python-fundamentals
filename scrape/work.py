#Web scraping library

__author__ = 'pangolin'

#Only import the libraries we use in this file
import io     #Use this to fix encoding
import scrape_lib


##An example
# r = get('http://statsforchange.org') #Get the data
# print 'status', r.status_code        #See httpstatus.es for codes
# print 'initial text:', r.text[:40]   #See some of the data
# tree = html.fromstring(r.text)   #Make a tree from the data
# print tree.body.text_content()   #See text content from the tree

#A single page
# test_url = ['http://statsforchange.org']

#Multiple pages
# test_urls = ['http://statsforchange.org', 'http://sfbay.craigslist.org/mca/', 'https://news.google.com/news?ncl=d8ovgjSMjdF1F-MYvjH0A6BKPiD0M&q=detroit&lr=English&hl=en&sa=X&ei=-mb2U_ydDtC7ogSvh4HwCg&ved=0CCYQqgIwAA']

#Instead of defining the list here, we can import a list from a text file
 #We need readlines to make each line of the text file a separate list element
url_list = io.open('url.txt', 'r').readlines()
craigslist_url_list = io.open('craigslist_url.txt', 'r').readlines()


#Instead of defining the function here, we can call the function from another .py file (our python library)
 #Need to import the file at the beginning of this file
 #The file can contain multiple functions
 #The format is filename.function(list)
scrape_lib.save_web_to_file(url_list)
scrape_lib.craigslist_table(craigslist_url_list)





