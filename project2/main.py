from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.iplt20.com/auction/2023'
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_ = "ih-td-tab auction-tbl")
title =  table.find_all("th")
# print(table)
# print(title)

header = []
for i in title:
    name = i.text
    header.append(name)

df = pd.DataFrame(columns=header)

rows = table.find_all("tr")
# print(rows)

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_ = "ih-pt-ic")
    data = i.find_all("td")
    row = [tr.text for tr in data] #list comprehension
    length = len(df)
    df.loc[length] = row

print(df)

df.to_csv("IPL Auction stats.csv")