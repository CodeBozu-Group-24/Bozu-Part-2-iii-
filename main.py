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
    try:
        writingFinal1 = getTextFromArticle(link).encode("ascii", "ignore").decode()
        writingFinal1 = re.sub("\n", " ", writingFinal1)
        writings1.append(writingFinal1)
    except AttributeError:
        writings1.append('No Text')    

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

#POLITICO for Joe Biden
politico_bid = []
positivity4 = []
data_politico = requests.get("https://www.politico.com/news/magazine/2020/03/05/biden-2020-president-facts-what-you-should-know-campaign-121422").text
soup_politico = BeautifulSoup(data_politico, 'lxml')
txt2 = soup_politico.findAll('p', class_='story-text__paragraph')
#print(txt1.get_text())
for ele in txt2:
  politico_bid.append(ele.get_text())

for elements in politico_bid:
    sid_obj4 = SentimentIntensityAnalyzer()
    sentiment_dict4 = sid_obj4.polarity_scores(elements)
    positivity_score4 = sentiment_dict4['pos']*100
    positivity4.append(positivity_score4)

scores_politico.append(str(sum(positivity4)/len(positivity4)))

#POLITICO for Barack Obama
politico_ob = []
positivity5 = []
data_politico2 = requests.get('https://www.politico.com/story/2012/02/the-political-transformation-of-barack-obama-072644').text
soup_politico2 = BeautifulSoup(data_politico2, 'lxml')
txt = soup_politico2.findAll('p')
for ele in txt:
    politico_ob.append(ele.get_text())

for elements in politico_ob:
    sid_obj5 = SentimentIntensityAnalyzer()
    sentiment_dict5 = sid_obj5.polarity_scores(elements)
    positivity_score5 = sentiment_dict5['pos']*100
    positivity5.append(positivity_score5)

scores_politico.append(str(sum(positivity5)/len(positivity5)))

with open('news.csv', 'w') as f:
    writer_object = writer(f)
    writer_object.writerow(["Politician", "BBC", "Politico"])
    for i in range(len(politicians)):
        writer_object.writerow([politicians[i], scores_bbc[i], scores_politico[i]])
    f.close()   

    