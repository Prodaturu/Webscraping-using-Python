# Python Web Scraping Project: AJIO Men's Jackets and Coats Scraper

This project is a Python-based web scraper that navigates to the AJIO online store, specifically the men's jackets and coats section, and extracts the brand names and prices of the products. It uses the Selenium WebDriver for browser automation and BeautifulSoup for parsing the HTML.

## Project Description

The goal of this project is to automate the process of extracting product information from the AJIO online store. The script uses Selenium WebDriver to control a Chrome browser instance, navigates to the men's jackets and coats section, scrolls through the page to load all products, and then uses BeautifulSoup to parse the HTML and extract the brand names and prices. The extracted data is then visualized using matplotlib to create a bar chart showing the average price per brand.

The information extracted includes:

- Brand names of the products
- Prices of the products

## Technologies Used

- Python
- Selenium WebDriver
- BeautifulSoup
- matplotlib

## How to Run the Project

1. Ensure that you have Python installed on your machine.
2. Install the required Python libraries with the command `pip install -r requirements.txt`.
3. Run the script with the command `python main.py`.
4. The script will open a Chrome browser window, navigate to the AJIO online store, load all products in the men's jackets and coats section, extract the brand names and prices, and then create a bar chart showing the average price per brand.

## Sample Output

After running the script, a bar chart showing the average price per brand will be displayed.

## Requirements

This script requires the following Python packages:

- Selenium WebDriver
- BeautifulSoup
- matplotlib

You can install these packages using pip:

``` bash
pip install -r requirements.txt
```

In addition to the Python packages, this script also requires the ChromeDriver executable. The ChromeDriver version must be compatible with the installed version of the Chrome browser on your machine. The ChromeDriver executable is included in the GitHub repository in the `chromedriver_win32` directory. Please ensure that your Chrome browser version is compatible with this ChromeDriver version.

## Future Improvements

In the future, the project can be further enhanced in the following ways:

1. Adding error handling and robustness to handle various scenarios and edge cases.
2. Implementing additional data extraction techniques to capture more information from the webpage.
3. Storing scraped data in a database for further analysis and/or usage of data.

## Acknowledgements

This project was inspired by the need to automate the process of extracting product information from online stores for comparison and analysis. It demonstrates the power of Python and its libraries in automating web browser tasks and parsing HTML.
