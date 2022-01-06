#from psrt 2 of Bozu part 2

from os import remove
from bs4 import BeautifulSoup
import requests
from csv import reader
import pandas as pd

def getTextFromArticle(link:str):
    req = requests.get(link).text
    soup = BeautifulSoup(req, "lxml")
    article = soup.find("article", {"class":"ssrcss-1mc1y2-ArticleWrapper e1nh2i2l6"})
    textDivs = article.find_all("div", {"data-component":"text-block"})
    returnString = ""
    for textDiv in textDivs:
        childDiv = textDiv.find_all("p")
        for x in childDiv:
            returnString+= x.get_text()
        returnString += '\n'
    
    return returnString

def getMeanScores(csvfile:str):
    data = pd.read_csv(csvfile)
    scores = data["score"]
    mean = lambda l:sum(l)/len(l)
    return mean(scores)