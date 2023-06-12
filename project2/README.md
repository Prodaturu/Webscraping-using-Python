# Python Web Scraping Project: IPL Auction Stats

This project is a web scraper built with Python. It uses the BeautifulSoup and requests libraries to scrape IPL auction information from the 'IPL T20' website.

## Project Description

The goal of this project is to extract data about IPL auction from the 'IPL T20' website. We will send a GET request to the website's URL using the requests library and retrieve the HTML content of the webpage. Then, using BeautifulSoup with the "lxml" parser, we will parse the HTML and extract the desired information.

## Technologies Used

- Python
- BeautifulSoup
- requests
- pandas

## How to Run the Project

1. Ensure that you have Python installed on your machine.
2. Install the required Python libraries with the command 
`pip install -r requirements.txt` or `pip install requests beautifulsoup4 pandas`.
3. Run the script with the command `python main.py`.
4. The script will send a GET request to the target URL, scrape the webpage, and print the extracted information about the IPL auction. It will also save the data in a CSV file named "IPL Auction stats.csv".

## Sample Output

After running the script, the program will print the IPL auction stats in the console and save the same data in a CSV file. The data includes:

1. Player name
2. Team name
3. Role
4. Price
5. Status

## Future Improvements

In the future the project can be further enhanced in following ways:

1. Implement additional data extraction techniques to capture more information about the IPL auction.
2. Adding error handling and robustness to handle various scenarios and edge cases.
3. Enhance the data storage mechanism to support large scale data.

## Acknowledgements

This project was inspired by the tutorial ["Python Web Scraping | What to study, Salary & Packages, Application | Simply Explained"](https://www.youtube.com/watch?v=2UTa6eTDdWc&list=PLjVLYmrlmjGfSYkgH-_jgC8KMxyRzq7US).
