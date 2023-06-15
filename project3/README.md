# Python Web Scraping Project: Flipkart Mobile Data Scraper

This project is a Python-based web scraper that extracts mobile phone data from the Flipkart website. It uses the BeautifulSoup and requests libraries to scrape the data and pandas to store and export the data to a CSV file.

## Project Description

The goal of this project is to extract data about mobile phones priced above 40,000 INR from the Flipkart website. The script sends a GET request to the website's URL using the requests library and retrieves the HTML content of the webpage. Then, using BeautifulSoup with the "lxml" parser, it parses the HTML and extracts the desired information.

The information extracted includes:

- Product Name
- Price
- Description

The script iterates over multiple pages of search results, extracting data from each page and storing it in a pandas DataFrame. Finally, the DataFrame is exported to a CSV file.

## Technologies Used

- Python
- BeautifulSoup
- requests
- pandas

## How to Run the Project

1. Ensure that you have Python installed on your machine.
2. Install the required Python libraries with the command `pip install -r requirements.txt` or `pip install requests beautifulsoup4 pandas`.
3. Run the script with the command `python main.py`.
4. The script will send a GET request to the target URL, scrape the webpage, and print the extracted information about the mobile phones. The data will be saved to a CSV file named "project3.csv".

## Sample Output

After running the script, the program will print the following info about mobile phones in the console:

1. Product Name: Extracted from the "div" tags with the class "_4rR01T".
2. Prices: Extracted from the "div" tags with the class "_30jeq3 _1_WHN1".
3. Description: Extracted from the "ul" tags with the class "_1xgFaf".

This information will also be saved to a CSV file.

## Future Improvements

In the future, the project can be further enhanced in the following ways:

1. Adding error handling and robustness to handle various scenarios and edge cases.
2. Implementing additional data extraction techniques to capture more information from the webpage.
3. Storing scraped data in a database for further analysis and/or usage of data.

## Acknowledgements

This project was inspired by the need to gather data for analysis and decision-making purposes. It demonstrates the power of Python and its libraries in extracting useful information from the web.
