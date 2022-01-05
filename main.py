from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import writer
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

#print(NewsSources)
NewsSources.insert(0, 'Politician')

with open('news.csv', 'w') as f:
    writer_object = writer(f)
    writer_object.writerow(NewsSources)
    f.close()   

politicians = []
with open('details.csv', 'r') as f:
    reader = csv.reader(f)
    amr_csv = list(reader)
    for row in amr_csv[1:]:
        politicians.append(row[0])
    f.close()

#the main list of politicians without repition of names
politicians_reduced = []
for ele in politicians:
    if ele not in politicians_reduced:
        politicians_reduced.append(ele)

#iterate through each politician and search about them in each news channel

