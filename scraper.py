from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_links_from_url(url, filename):
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the URL
    driver.get(url)

    # Wait for the dynamic content to load
    time.sleep(5)

    # Find the grey box using the XPath
    try:
        grey_box = driver.find_element(
            "xpath", "/html/body/main/div/div/section/ul")
        # Find all 'a' tags within the grey box
        links_in_grey_box = grey_box.find_elements("tag name", 'a')

        # Extract the URLs
        urls = [link.get_attribute('href') for link in links_in_grey_box]
    except Exception as e:
        print(f"Failed to find or process elements in {url}, error: {e}")
        urls = []

    # Close the driver
    driver.quit()

    # Update the text file with new URLs
    update_file_with_urls(filename, urls)


def update_file_with_urls(filename, urls):
    # Read existing URLs from file
    existing_urls = set()
    try:
        with open(filename, "r") as file:
            existing_urls.update(file.read().splitlines())
    except FileNotFoundError:
        print(f"No existing file found, a new one will be created: {filename}")

    # Write only new URLs to file
    with open(filename, "a") as file:
        for url in urls:
            if url not in existing_urls:
                file.write(url + '\n')
                print(f"Added URL to file: {url}")
            else:
                print(f"URL already in file: {url}")


# URLs to process
urls = [
    'https://support.gigpro.com/hc/en-us/sections/10396868544404-How-Gigpro-Works',
    'https://support.gigpro.com/hc/en-us/sections/10396880517652-Pro-Payments',
    'https://support.gigpro.com/hc/en-us/sections/10396915184148-Stripe-Help',
    'https://support.gigpro.com/hc/en-us/sections/10397009984788-Profile-Help',
    'https://support.gigpro.com/hc/en-us/sections/10396935809684-Gigs-Help',
    'https://support.gigpro.com/hc/en-us/sections/10397709752468-How-does-Gigpro-Work',
    'https://support.gigpro.com/hc/en-us/sections/10397706188308-Account-Management',
    'https://support.gigpro.com/hc/en-us/sections/10397676348436-Posting-Gigs',
    'https://support.gigpro.com/hc/en-us/sections/10397649422612-Selecting-Paying-Pros',
]

# Filename for storing URLs
filename = "unique_urls.txt"

# Process each URL
for url in urls:
    get_links_from_url(url, filename)
