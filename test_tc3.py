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


class TestTC3:
    @pytest.fixture(scope='class')
    def driver(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        service = FirefoxService(executable_path='drivers/geckodriver.exe')
        driver = webdriver.Firefox(service=service, options=options)
        yield driver
        driver.quit()

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        driver.set_window_size(1603, 947)
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_by_tag_locator(self, driver):
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Znaleziono: {len(links)}")
        for e in links:
            if e.text:
                print(e.text)
