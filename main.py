# coding=utf-8

import requests
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org/wiki/List_of_minor_planets:_"
date = "January 20, 1998"

def search (url): 
    print url
    r = requests.get (url);
    soup = BeautifulSoup (r.content, 'html.parser')
    tables = soup.find_all ("table", { "class": "wikitable" })
    for table in tables:
        lines = table.find_all ("tr")
        for line in lines:
            items = line.find_all ("td")
            if len(items) < 3:
                continue
            if (items[2].get_text () == date):
                print items[0].get_text ()

for i in range (1, 600000, 1000):
    search (base_url + str (i) + '-' + str (i + 999))

