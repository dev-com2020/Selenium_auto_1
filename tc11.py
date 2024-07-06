from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class IAmTheEventListener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver):
        print(f"Before navigate to: {url}")

    def after_navigate_to(self, url: str, driver):
        print(f"After navigate to: {url}")

    def before_navigate_back(self, driver):
        print("Before navigate back")

    def after_navigate_back(self, driver):
        print("After navigate back")


def main():
    def run_test(browser_name):
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.set_capability('browserName', 'chrome')
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.set_capability('browserName', 'firefox')
        elif browser_name == 'edge':
            options = webdriver.EdgeOptions()
            options.set_capability('browserName', 'MicrosoftEdge')
        else:
            raise ValueError('Nieznana przeglądarka {}'.format(browser_name))

        options.add_argument('--headless')

        driver = webdriver.Remote(
            command_executor='http://192.168.31.240:4444/wd/hub',
            options=options)

        try:
            event_listener = IAmTheEventListener()
            event_firing_driver = EventFiringWebDriver(driver, event_listener)

            event_firing_driver.get("https://www.alx.pl")
            event_firing_driver.get("http://www.google.pl")
            event_firing_driver.back()
        finally:
            driver.close()
            driver.quit()

    for browser in ['chrome', 'firefox', 'edge']:
        run_test(browser)


if __name__ == '__main__':
    main()
