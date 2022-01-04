from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import reader
import pandas as pd
import re

data = requests.get('https://en.wikipedia.org/wiki/News_media_in_the_United_States').text
soup = BeautifulSoup(data, 'lxml')
list1 = soup.findAll('h4')



table = soup.find("table", {"class":"wikitable sortable"})
rows = table.find_all("tr")
rows = rows[1:]
NewsSources = []
for row in rows:
    td = row.find("td")
    NameOfSource = re.sub("\n", " ",td.get_text())
    NewsSources.append(NameOfSource)

print(NewsSources)