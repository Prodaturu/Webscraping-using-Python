import requests
from bs4 import BeautifulSoup
#.☝️ imports 'requests' and 'bs4' libraries

#. 👇 creating a url 
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url) #, sends a GET request to spec URL and stores in var 'r'. 
#print(r)

#. Using BeautifulSoup to scrap data
soup = BeautifulSoup(r.text, "lxml") #lxml is the format code

#. Extracting data

boxes = soup.find_all("div", class_ = "col-sm-4 col-lg-4 col-md4" ) #, Searches all div elements, with given class.
print(len(boxes)) #, No of 'div' tag having the given class.

names = soup.find_all("a", class_ = 'title') #, searches all 'a' tags with 'title' class.
#print(names)
for i in names:
    print(i.text)

prices = soup.find_all("h4", class_ = "pull-right price")
for i in prices:
    print(i.text)