from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.links = (By.TAG_NAME, "a")

    def tag_locator(self):
        linki = self.driver.find_elements(*self.links)
        print(f"Znaleziono: {len(linki)}")
        zestaw = []
        for e in linki:
            if e.text:
                zestaw.append(e.text)
        return str(zestaw)
