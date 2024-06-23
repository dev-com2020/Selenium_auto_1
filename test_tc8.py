# Generated by Selenium IDE
import os
from datetime import datetime

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.devtools.v85.network import CookieParam

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTc6:

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

    def test_load_cookies(self, driver):
        try:
            data_file_path = './cookies.txt'
            if os.path.exists(data_file_path):
                with open(data_file_path, 'r') as data_file:
                    lines = data_file.readlines()
                    for line in lines:
                        tokens = line.strip().split(';')
                        name = tokens[0]
                        value = tokens[1]
                        domain = tokens[2]
                        path = tokens[3]
                        expiry = tokens[4]
                        if expiry != 'N/A':
                            expiry = datetime.utcfromtimestamp(float(expiry))
                        else:
                            expiry = None
                        is_secure = tokens[5].lower() == 'true'
                        cookie = CookieParam(name=name, value=value, domain=domain, path=path, expires=expiry,
                                             secure=is_secure)
                        driver.add_cookie(cookie)
                title = driver.find_element(By.CLASS_NAME, 'hello').text
                assert title == 'Hello, ester tester tester!'
            else:
                print(f"{data_file_path} nie istnieje")
        except Exception as e:
            print(e)
