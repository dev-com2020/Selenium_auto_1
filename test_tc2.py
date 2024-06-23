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


class TestTc2:

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        driver.set_window_size(1603, 947)
        driver.get("http://demo-store.seleniumacademy.com/")

    @pytest.mark.parametrize(
        "search_term, expected_title", [
            pytest.param("blazer", "Search results for: 'blazer'", id="wyszukuje blazer"),
            pytest.param("shirts", "Search results for: 'shirts'", id="wyszukuje shirts"),
        ]
    )
    def test_search(self, driver, search_term, expected_title):
        driver.find_element(By.ID, "search").send_keys(search_term)
        driver.find_element(By.CSS_SELECTOR, ".search-button").click()
        assert driver.title.lower() == expected_title.lower()
