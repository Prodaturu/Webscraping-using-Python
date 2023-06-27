# Python Web Scraping Project: LinkedIn Profile Scraper

This project is a Python-based web scraper that navigates to Google, searches for a specific LinkedIn profile, and takes a screenshot of the profile page. It uses the Selenium WebDriver for browser automation.

## Project Description

The goal of this project is to automate the process of searching for a specific LinkedIn profile via Google and taking a screenshot of the profile page. The script uses Selenium WebDriver to control a Chrome browser instance, navigates to Google, enters the search query, clicks on the appropriate search result, and finally takes a screenshot of the profile page.

The information extracted includes:

- Screenshot of the LinkedIn profile page

## Technologies Used

- Python
- Selenium WebDriver

## How to Run the Project

1. Ensure that you have Python installed on your machine.
2. Install the required Python libraries with the command `pip install -r requirements.txt`.
3. Run the script with the command `python main.py`.
4. The script will open a Chrome browser window, navigate to Google, perform the search, navigate to the LinkedIn profile, and take a screenshot. The screenshot will be saved to a specified directory.

## Sample Output

After running the script, a screenshot of the LinkedIn profile page will be saved in the specified directory.

## Requirements

This script requires the following Python package:

- Selenium WebDriver

You can install this package using pip:

``` bash
pip install -r requirements.txt
```

In addition to the Python package, this script also requires the ChromeDriver executable. The ChromeDriver version must be compatible with the installed version of the Chrome browser on your machine. The ChromeDriver executable is included in the GitHub repository in the `chromedriver_win32` directory. Please ensure that your Chrome browser version is compatible with this ChromeDriver version.

## Future Improvements

In the future, the project can be further enhanced in the following ways:

1. Adding error handling and robustness to handle various scenarios and edge cases.
2. Implementing additional data extraction techniques to capture more information from the webpage.
3. Storing scraped data in a database for further analysis and/or usage of data.

## Acknowledgements

This project was inspired by the need to automate the process of searching for specific LinkedIn profiles and capturing information from them. It demonstrates the power of Python and its libraries in automating web browser tasks.
