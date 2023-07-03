from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#: Set up ChromeDriver and launch a new Chrome browser instance.
s = Service("./chromedriver_win32/chromedriver.exe")    #, Boiler-plate code
driver = webdriver.Chrome(service=s)    #, Boiler-plate code

#: Load the url in the browser.
url = "https://www.ajio.com/men-jackets-coats/c/830216010?query=%3Arelevance%3Averticalsizegroupformat%3AS&gridColumns=3&segmentIds="
driver.get(url)
time.sleep(5)
height = driver.execute_script("return document.body.scrollHeight")
i = 0 # for testing
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height = new_height
    
    # for testing
    i+=1
    if i > 2:
        break

#. Find all the products and their prices on the page:

#: Get page source and create a BeautifulSoup object:
html = driver.page_source   #, Boiler-plate code
soup = BeautifulSoup(html, "html.parser")   #, Boiler-plate code

#: Find  all price's on the page:
prices = soup.find_all("span", class_="price")
pricesList = [price.text.replace("₹","").replace(",","").strip() for price in prices]

#: Find all product's on the page:
brandNames = soup.find_all("div", class_="nameCls")
brandNames_List = [brandName.text for brandName in brandNames]

#. Comparing Product names and prices on a graph using matplotlib:

print("Product names length: ", len(brandNames_List), "\nPrices length: ", len(pricesList))
time.sleep(3)

pricesList = [int(price.replace(",",""))
for price in pricesList]   #, converting to integers for plotting
plt.figure(figsize=(10,8))
plt.bar(brandNames, pricesList)

#: Add labels and title:
plt.xlabel('Product Names')
plt.ylabel('Prices')
plt.title('Products and Prices')
plt.xticks(rotation=90) #, Rotating x-axis labels

plt.show()