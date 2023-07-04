from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

#. Locating chrome driver and opening the browser :
path = "./chromedriver_win32/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)

#. Opening the website and searching what we need:
driver.get("https://www.google.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('"Saikiran Prodaturu" Linkedin')   #, +"" To search for the exact phrase
search_box.send_keys(Keys.ENTER)
time.sleep(3) #. Waiting for the page to load

driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a').click()
time.sleep(3)

if not os.path.exists('./project4/screenshots'):
    os.makedirs('./project4/screenshots')
driver.save_screenshot("./project4/screenshots/SaikiranProdaturu_LinkedIn.png")
time.sleep(3)
