from bs4 import BeautifulSoup
import requests
import csv
import wolframalpha
import matplotlib.pyplot as plt
from csv import reader
import pandas as pd

data = requests.get('https://en.wikipedia.org/wiki/News_media_in_the_United_States').text
soup = BeautifulSoup(data, 'lxml')
list1 = soup.findAll('h4')
