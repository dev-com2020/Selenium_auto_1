import pytest

from PageObject.pages.main_page import MainPage


def test_links_locator(driver):
    driver.get("http://demo-store.seleniumacademy.com/")
    main_page = MainPage(driver)
    funkcja = main_page.tag_locator()
    assert "PINTEREST" in funkcja

