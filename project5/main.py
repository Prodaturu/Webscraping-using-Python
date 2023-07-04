from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import defaultdict

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
pricesList = [int(price.text.replace("₹","").replace(",","").strip()) for price in prices]

#: Find all product's on the page:
brandNames = soup.find_all("div", class_="brand")
brandNames_List = [brandName.text for brandName in brandNames]

#. Calculate average price per brand:

#: Initialize a dictionary to store the total price and count for each brand
brand_data = defaultdict(lambda: [0, 0]) # default value is a list [0, 0]

for brand, price in zip(brandNames_List, pricesList):
    brand_data[brand][0] += price # add price to total
    brand_data[brand][1] += 1 # increment count

#: Calculate average price for each brand
avg_prices = {brand: total/count for brand, (total, count) in brand_data.items()}

#. Comparing Brand names and average prices on a graph using matplotlib:

brands = list(avg_prices.keys())
avg_prices = list(avg_prices.values())

#: plotting the graph of brands (x) vs avg_prices (y):
plt.figure(figsize=(15,8))
plt.bar(brands, avg_prices)

#: Add labels and title:
plt.xlabel('Brand Names', fontsize = 10)
plt.ylabel('Average Prices', fontsize = 12)
plt.title('Average Price per Brand')
plt.xticks(rotation=90) #, Rotating x-axis labels

plt.show()
