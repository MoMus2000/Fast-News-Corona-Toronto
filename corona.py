import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime

now = datetime.datetime.now()
date_string = now.strftime('%m-%d')
date_string+="-20"


cnn = requests.get("https://www.cnn.com/world/live-news/coronavirus-pandemic-"+date_string+"-intl/index.html")
cp24 = requests.get("https://www.cp24.com/news")
soup = BeautifulSoup(cnn.content,"html.parser")
soups = BeautifulSoup(cp24.content,"html.parser")

Headlines = soup.find_all(class_="post-headlinestyles__Headline-sc-2ts3cz-1 gzgZOi")
Headlines2 = soups.find_all(class_="teaserTitle")

heads = [i.get_text() for i in Headlines]
heads2 = [j.get_text() for j in Headlines2]


print("\n")
for Item in heads:
    print(Item.rjust(8), sep='/n')
