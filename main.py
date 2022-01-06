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
scores_bbc = []

#BBC for Donald Trump
data1 = requests.get('https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump').text
soup1 = BeautifulSoup(data1, 'lxml')
titles1 = soup1.findAll('a', class_='qa-heading-link lx-stream-post__header-link')

title_text1 = []
for title in titles1:
    title_text1.append(title.get_text())

#links = []
writings1 = []
for title in titles1:
    link = "https://www.bbc.com"+title["href"]
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    writingFinal1 = getTextFromArticle(link).encode("ascii", "ignore").decode()
    writingFinal1 = re.sub("\n", " ", writingFinal1)
    writings1.append(writingFinal1)

positivity1 = []    
for writing in writings1:
    sid_obj1 = SentimentIntensityAnalyzer()
    sentiment_dict1 = sid_obj1.polarity_scores(writing)
    positivity_score1 = sentiment_dict1['pos']*100
    positivity1.append(positivity_score1)

scores_bbc.append(str(sum(positivity1)/len(positivity1)))

#BBC for Joe Biden
data2 = requests.get('https://www.bbc.co.uk/search?q=Joe+Biden').text
soup2 = BeautifulSoup(data2, 'lxml')
titles2 = soup2.findAll('a', href=True, class_='ssrcss-atl1po-PromoLink e1f5wbog0')

title_text2 = []
for title in titles2:
    title_text2.append(title.get_text())

links = []    
subs = 'href'
res = [str(i) for i in titles2 if subs in str(i)]
for ele in res:
    link = ele.split(' ')[3]
    i = link.index('"')
    f = link.index('>')
    links.append(link[(i+1):(f-1)])

writings2 = []
for link in links:
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    try:
        writingFinal2 = getTextFromArticle(link).encode("ascii", "ignore").decode()
        writingFinal2 = re.sub("\n", " ", writingFinal2)
        writings2.append(writingFinal2)
    except AttributeError:
        writings2.append('No text existing currenly.')

positivity2 = []    
for writing in writings2:
    sid_obj2 = SentimentIntensityAnalyzer()
    sentiment_dict2 = sid_obj2.polarity_scores(writing)
    positivity_score2 = sentiment_dict2['pos']*100
    positivity2.append(positivity_score2)

scores_bbc.append(str(sum(positivity2)/len(positivity2)))


#BBC News for Barack Obama
data3 = requests.get('https://www.bbc.co.uk/search?q=Barack+Obama').text
soup3 = BeautifulSoup(data3, 'lxml')
titles3 = soup3.findAll('a', href=True, class_='ssrcss-atl1po-PromoLink e1f5wbog0')

title_text3 = []
for title in titles3:
    title_text3.append(title.get_text())

links3 = []    
subs = 'href'
res = [str(i) for i in titles3 if subs in str(i)]
for ele in res:
    link = ele.split(' ')[3]
    i = link.index('"')
    f = link.index('>')
    links3.append(link[(i+1):(f-1)])

writings3 = []
for link in links3:
    #data_new = requests.get(link).text
    #soup_new = BeautifulSoup(data_new, 'lxml')
    try:
        writingFinal3 = getTextFromArticle(link).encode("ascii", "ignore").decode()
        writingFinal3 = re.sub("\n", " ", writingFinal3)
        writings3.append(writingFinal3)
    except AttributeError:
        writings3.append('No text existing currenly.')

positivity3 = []    
for writing in writings3:
    sid_obj3 = SentimentIntensityAnalyzer()
    sentiment_dict3 = sid_obj3.polarity_scores(writing)
    positivity_score3 = sentiment_dict3['pos']*100
    positivity3.append(positivity_score3)

scores_bbc.append(str(sum(positivity3)/len(positivity3)))


scores_politico = []

#POLITICO for Donald Trump
scores_politico.append('6.975')
