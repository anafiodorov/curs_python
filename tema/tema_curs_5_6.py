
# SA INSTALEZ MYSQL!!!!!!!
# SA INSTALEZ MOODLE
from bs4 import BeautifulSoup
import requests


def print_with_space(word, size):
    len_to_add = size - len(word)
    final_word = "|" + word
    for _ in range(1, len_to_add):
        final_word = final_word + " "
    with open("web_scraper.txt", mode='a') as new_file:
      new_file.write(final_word)


URL = 'https://finance.yahoo.com/most-active'
r = requests.get(URL, headers={'Cache-Control': 'no-cache'})
soup = BeautifulSoup(r.content, 'html.parser')

# clear file
with open("web_scraper.txt", mode='w') as new_file:
    new_file.truncate(0)

div = soup.find('div', attrs={'id': 'scr-res-table'})
table = div.find('table')
for row in table.findAll('tr', attrs={'class': 'simpTblRow'}):
    symbol = row.find('td', attrs={'aria-label': 'Symbol'}).text
    name = row.find('td', attrs={'aria-label': 'Name'}).text
    market_cap = row.find('td', attrs={'aria-label': 'Market Cap'}).text
    print_with_space(symbol, 10)
    print_with_space(name, 50)
    print_with_space(market_cap, 10)
    with open("web_scraper.txt", mode='a') as new_file:
        new_file.write("\n")

with open("web_scraper.txt", mode='r') as new_file:
    lines = new_file.readlines()
    for line in lines:
        print(line)