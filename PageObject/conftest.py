from selenium import webdriver
import pytest


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.set_capability('browserName', 'chrome')
        options.add_argument('--headless')
        driver = webdriver.Remote(
            command_executor='http://192.168.31.240:4444/wd/hub',
            options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_capability('browserName', 'firefox')
        options.add_argument('--headless')
        driver = webdriver.Remote(
            command_executor='http://192.168.31.240:4444/wd/hub',
            options=options)
    else:
        raise ValueError('Nieznana przeglądarka {}'.format(browser_name))

    yield driver
    driver.quit()