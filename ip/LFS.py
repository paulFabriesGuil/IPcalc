#! /bin/python

import requests
from bs4 import BeautifulSoup

url = "https://fr.linuxfromscratch.org/view/lfs-systemd-stable/chapter03/packages.html"
page = requests.get(url)
parser = BeautifulSoup(page.content, 'html.parser')

abc = parser.find_all('dl')
for a in abc:
    print(type(a))  
    #print(a.find_all('dt'))

for dd in abc:
    all_dd = dd.find_all('dd')
    for elem_dd in all_dd:
        print(elem_dd.find_all('p'))


"""
Structure des données :

row key dans dd
column key dans dt

"""