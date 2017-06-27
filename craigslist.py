import requests
from bs4 import BeautifulSoup

def cSpider(max_pages):
    page = 120
    while page < max_pages:
        url ='https://vancouver.craigslist.ca/search/cta?s=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':'result-title hdrlnk'}):
            title = link.string
            href='https://vancouver.craigslist.ca/'+link.get('href')
            get_single_item_data(href)
            print('{} {:>150}'.format(title, href))
        pages+=120

def get_single_item_data(item_url):
    source_code=requests.get(item_url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for item_name in soup.findAll('span',{'class':'price'}):
        print (item_name.string)
        
cSpider(240)
