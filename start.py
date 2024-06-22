import locale
import sys

from selenium import webdriver

from test_tc1 import TestTc1
import pytest


@pytest.mark.parametrize("browser", ['chrome', 'firefox'])
def test_run(browser, request):
    headless = request.config.getoption("--headless")
    driver = request.getfixturevalue("browser_fixture")
    test = TestTc1()
    try:
        test.test_tc1(driver)
    except Exception as e:
        screenshot_name = f"screenshot_{browser}_{headless}.png"
        test.save_screenshot(driver, screenshot_name)
        print(f"Saved screenshot: {screenshot_name}")
        raise e


@pytest.fixture
def browser_fixture(request):
    browser_param = request.config.getoption("--browser")
    headless_param = request.config.getoption("--headless")

    if browser_param == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless_param:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    elif browser_param == 'chrome':
        options = webdriver.ChromeOptions()
        if headless_param:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception("Unsupported browser")

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def setup_locale():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    yield
    locale.setlocale(locale.LC_ALL, None)
