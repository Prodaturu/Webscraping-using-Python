# Python Web Scraping Project

This project is a simple web scraper built with Python. It uses the BeautifulSoup and requests libraries to scrape book information from the 'Books to Scrape' website and stores the data in a CSV file.

## Project Description

The goal of this project is to extract data about laptops from the 'Web Scraper' website. We will send a GET request to the website's URL using the requests library and retrieve the HTML content of the webpage. Then, using BeautifulSoup with the "lxml" parser, we will parse the HTML and extract the desired information.

## Technologies Used

- Python
- BeautifulSoup
- requests

## How to Run the Project

1. Ensure that you have Python installed on your machine.
2. Install the required Python libraries with the command 
`pip install -r requirements.txt` or `pip install requests beautifulsoup4`.
3. Run the script with the command `python main.py`.
4. The script will send a GET request to the target URL, scrape the webpage, and print the extracted information about the laptops.

## Sample Output

After running the script, the program will print following info about laptops in the console:

1. Number of div elements with class "col-sm-4 col-lg-4 col-md4" found on the webpage.
2. Names of Laptops extracted from the "a" tags with "title" class.
3. Prices of laptops extracted from the "h4" tags with the class "pull-right price"

## Future Improvements

In the future the project can be further enhanced in following ways:

1. Storing scraped data in a file or a database for further analysis and / or usage of data.
2. Implement additional data extraction techniques to capture more information about from the webpage.
3. Adding error handling and robustness to handle various scenarios and edge cases.

## Acknowledgements

This project was inspired by the tutorial ["Python Web Scraping | What to study, Salary & Packages, Application | Simply Explained"](https://www.youtube.com/watch?v=2UTa6eTDdWc&list=PLjVLYmrlmjGfSYkgH-_jgC8KMxyRzq7US).
