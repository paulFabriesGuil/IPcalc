#! /bin/python

import requests
from bs4 import BeautifulSoup

url = "https://strategywiki.org/wiki/Total_Annihilation/Units"
page = requests.get(url)
parser = BeautifulSoup(page.content, 'html.parser')

for table in parser.find_all("table"):
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            print(td.get_text())
        for th in tr.find_all("th"):
            print(th.get_text()) 