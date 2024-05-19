import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# Set up argument parsing
parser = argparse.ArgumentParser(description="Web Link Checker using Selenium")
parser.add_argument("-d", "--domain", required=True, help="Domain Name; EX: https://test.com")
args = parser.parse_args()

# Path to GeckoDriver
gecko_driver_path = '/usr/bin/geckodriver'  # Ensure this is the correct path

# Initialize WebDriver for Firefox
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open the specified website
driver.get(args.domain)

# Function to safely get the href attribute
def get_href(link):
    try:
        return link.get_attribute('href')
    except StaleElementReferenceException:
        return None

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, 'a')

# Extract and print the href attribute of each link
for link in links:
    url = get_href(link)
    if url:  # Check if href is not None
        print(url)

# Close the browser
driver.quit()

