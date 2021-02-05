#import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.barnesandnoble.com/b/the-new-york-times-bestsellers-hardcover-nonfiction/_/N-1p5q"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

ny_best_seller_items = html_soup.find_all('div', class_='row topX-row')

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for ny in ny_best_seller_items:
    title = ny_best_seller.find('div', class_= 'col-lg-3 product-shelf-tile product-shelf-tile-book').text
    price = ny_best_seller.find('div', class_= 'product-shelf-pricing mt-s mb-s').text

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



