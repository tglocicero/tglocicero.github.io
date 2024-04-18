from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re


urls = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open("unique_urls.txt", "r") as file:
    lines = file.readlines()

with open("index.html", "w") as output_file:
    for url in lines:
        driver.get(url)
        unique_page_file_name = re.sub("https.*articles/", "", url)[:-1]
        colloquial_page_name = re.sub("-", " ", re.sub("([0-9]+-)", "", unique_page_file_name))
        fileToWrite = open(f"{unique_page_file_name}.html", "w")
        fileToWrite.write(driver.page_source)
        fileToWrite.close()
        output_file.write(
            f'<a href="/{unique_page_file_name}">{colloquial_page_name}</a>'
        )

