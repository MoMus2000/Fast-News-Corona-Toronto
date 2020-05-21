import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime

now = datetime.datetime.now()
date_string = now.strftime('%m-%d')
date_string+="-20"


cp24 = requests.get("https://www.cp24.com/news")
soups = BeautifulSoup(cp24.content,"html.parser")
Headlines2 = soups.find_all(class_="teaserTitle")
Teaser = soups.find_all(class_="lead-left teaserLead image")

news = []
for j in Teaser:
    heads = j.find("p")
    news.append(heads.text)


heads2 = [j.get_text() for j in Headlines2]

# for Items in heads2:
#     print(Items)
#     print(news)

res = "\n".join("{} {}".format(x, y) for x, y in zip(heads2, news))
print(res)
