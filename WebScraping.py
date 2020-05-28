import requests
from bs4 import BeautifulSoup



'''Scraping quotes.toscrape.com'''
url = "http://quotes.toscrape.com/"

response = requests.get(url)
bsoup = BeautifulSoup(response.text,'lxml')

quotes = bsoup.findAll('span',class_='text')

authors = bsoup.findAll('small',class_='author')

tags = bsoup.find_all('div',class_='tags')

for i in range(0,len(quotes)):
    print("{}. {}".format(i+1,quotes[i].text))
    print('By-',authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    print('Quote tags are:')
    print(','.join(qT.text for qT in quoteTags))
    print('\n')



'''Scraping scrapingclub.com'''
url = "https://scrapingclub.com/exercise/list_basic/"

response = requests.get(url)
bsoup = BeautifulSoup(response.text,'lxml')

items = bsoup.find_all('div',class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4',class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('{}. Item Name:{}, Price:{}'.format(count,itemName,itemPrice),end='')
    count += 1
    print('\n')

list_of_pages = bsoup.find('ul',class_='pagination')
pages = list_of_pages.find_all('a',class_='page-link')
urls = []

for p in pages:
    pageNum = int(p.text) if p.text.isdigit() else None
    if pageNum != None:
        url = p.get('href')
        urls.append(url)

for u in urls:
    url = "https://scrapingclub.com/exercise/list_basic/"+u

    response = requests.get(url)
    bsoup = BeautifulSoup(response.text,'lxml')
    items = bsoup.find_all('div',class_='col-lg-4 col-md-6 mb-4')

    page_no = u[-1]
    print('List of items and price for page no.{}'.format(int(page_no)))
    count = 1
    for i in items:
        itemName = i.find('h4',class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('{}. Item Name:{}, Price:{}'.format(count,itemName,itemPrice),end='')
        count += 1
        print('\n')
    
    


