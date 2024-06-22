def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome', help="wybor przegladarki")
    parser.addoption("--headless", action="store", help="opcja headless")
