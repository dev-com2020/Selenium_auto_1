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


# def main():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)

def main():
    options = webdriver.ChromeOptions()
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


if __name__ == '__main__':
    main()
