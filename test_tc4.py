# Generate by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    service = FirefoxService(executable_path='drivers/geckodriver.exe')

    firefox_profilie = webdriver.FirefoxProfile()
    firefox_profilie.set_preference(
        "general.useragent.override", "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004 "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36")
    options.profile = firefox_profilie

    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup(driver):
    driver.set_window_size(1603, 947)
    driver.get("http://demo-store.seleniumacademy.com/")


def test_by_tag_locator(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Znaleziono: {len(links)}")
    for e in links:
        if e.text:
            print(e.text)
