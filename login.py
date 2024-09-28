import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def driver():
    service=Service("C:/Users/CSE-JnU/Desktop/Chromedriver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.get('https://ems-test.amaderit.net/')

    print("Page title is:",driver.title)
    driver.quit()