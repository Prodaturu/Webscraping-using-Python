from bs4 import BeautifulSoup
import requests
import pandas as pd

data_frame = []
for i in range(1,11):
    url = "https://www.flipkart.com/search?q=mobile+above+40000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_17_sc_na_ps&otracker1=AS_Query_OrganicAutoSuggest_1_17_sc_na_ps&as-pos=1&as-type=RECENT&suggestionId=mobile+above+40000&requestId=b338a1e4-d601-4906-a7e1-d878ae50d482&as-searchtext=mobiles+above+40k&p%5B%5D=facets.price_range.from%3D30000&p%5B%5D=facets.price_range.to%3DMax&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    soupBox = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    product_name = []
    product_prices = []
    product_description = []
    # product_reviews = []

        #. soup = BeautifulSoup(r.content, 'html.parser')
        # nextPageURL = soup.find("a", class_ = "_101LKTO3").get("href")
        # completeNextPageURL = "https://www.flipkart.com/" + nextPageURL
        # url = completeNextPageURL
        # print(completeNextPageURL) #prints url for each page

    names =  soupBox.find_all("div", class_ = "_4rR01T")
    for name in names:
        product_name.append(name.text)

    prices = soupBox.find_all("div", class_="_30jeq3 _1_WHN1")
    for price in prices:
        product_prices.append(price.text)

    descriptions = soupBox.find_all("ul", class_="_1xgFaf")
    for description in descriptions:
        product_description.append(description.text)

    # reviews = soupBox.find_all("div", class_="_3LWZlK")
    # for review in reviews:
    #     if review is not None:
    #         product_reviews.append(review.text)
    #     else:
    #         product_reviews.append('0')

    #: creating a df for present page
    df = pd.DataFrame({
        "Product Name" : product_name,
        "Prices" : product_prices,
        "Description" : product_description,
        # "Reviews" : product_reviews
        })
    data_frame.append(df)

    # print(len(product_name))
    # print(len(product_prices))
    # print(len(product_description))
    # print(len(product_reviews))

df_final = pd.concat(data_frame, ignore_index = True)
df_final.to_csv("project3.csv", index= False)
