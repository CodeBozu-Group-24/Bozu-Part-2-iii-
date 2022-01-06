from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import writer
import pandas as pd
from scraper import getTextFromArticle, getMeanScores
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
'''
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
'''
politicians = ['Donald Trump', 'Joe Biden', 'Barack Obama']
scores = []
#Donald Trump
data = requests.get('https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump').text
soup = BeautifulSoup(data, 'lxml')
titles = soup.findAll('a', class_='qa-heading-link lx-stream-post__header-link')



title_text = []
for title in titles:
    title_text.append(title.get_text())

#links = []
writings = []
for title in titles:
    link = "https://www.bbc.com"+title["href"]
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    writingFinal = getTextFromArticle(link).encode("ascii", "ignore").decode()
    writingFinal = re.sub("\n", " ", writingFinal)
    writings.append(writingFinal)

positivity = []    
for writing in writings:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(writing)
    positivity_score = sentiment_dict['pos']*100
    positivity.append(positivity_score)

scores.append(str(sum(positivity)/len(positivity)))
#iterate through each politician and search about them in each news channel

