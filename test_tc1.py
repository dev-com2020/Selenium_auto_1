# Generated by Selenium IDE
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


class TestTc1():
    def setup_method(self, method, browser='chrome', headless=True):
        if browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=options)

        elif browser == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise Exception('Niedostępna przeglądarka')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tc1(self):
        self.driver.get("http://seleniumdemo.com/")
        self.driver.set_window_size(1800, 993)
        self.driver.find_element(By.CSS_SELECTOR, ".sek-btn-text").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "View cart").click()
        self.driver.find_element(By.LINK_TEXT, "×").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row .branding-row span").click()

