from bs4 import BeautifulSoup as bs

with open('jameslong.name_locallist.html', 'r') as url:
    soup = bs(url, 'html.parser')

print(soup)
