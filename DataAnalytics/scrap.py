#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml#"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 
