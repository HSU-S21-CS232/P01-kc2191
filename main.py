#import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import os, os.path, csv

url_to_scrape = "https://www.northtownbooks.com/local-0"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

northtown_local_book_items = html_soup.find_all('div', class_='abaproduct-content')

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for local_books in northtown_local_book_items:
    title = northtown_local_book_items.find('div', class_= 'abaproduct-title').text
    price = northtown_local_book_items.find('div', class_= 'abaproduct-price').text

f.write(title + ',' + price)

f.close()
#url = 'http://docs.python.org/'
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

#private email
#webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

#school email
#webbrowser.open('https://mail.google.com/mail/u/1/#inbox')

#proudmary coffee
#webbrowser.open('https://proudmarycoffee.com/collections/all-coffee')

#poetrycollection
#webbrowser.open('https://drive.google.com/drive/u/0/folders/1qBe4SggQ-2syCERrBpL5QsRrLPgOoj-R')

#ufcnews
#webbrowser.open('https://twitter.com/ufcnews?lang=en')

#canvas
#webbrowser.open('https://canvas.humboldt.edu/')



