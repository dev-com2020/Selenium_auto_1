# Generated by Selenium IDE
import os

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


class TestTc7:

    @pytest.fixture(scope='class')
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        driver.set_window_size(1603, 947)
        driver.get("http://demo-store.seleniumacademy.com/customer/account/login/")
        driver.implicitly_wait(5)

    def test_store_cookies(self, driver):
        driver.find_element(By.ID, "email").send_keys("user@seleniumacademy.com")
        driver.find_element(By.ID, "pass").send_keys("tester")
        driver.find_element(By.ID, "send2").submit()

        cookies = driver.get_cookies()
        data_file = "./cookies.txt"
        os.makedirs(os.path.dirname(data_file), exist_ok=True)

        with open(data_file, "w") as file:
            for cookie in cookies:
                file.write(f"{cookie['name']};{cookie['value']};{cookie['domain']};"
                           f"{cookie['path']};{cookie.get('expiry','N/A')};{cookie['secure']}\n")

