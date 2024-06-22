from test_tc1 import TestTc1
import pytest


@pytest.mark.parametrize("browser, headless", [
    ('chrome', True),
    ('firefox', True)
])
def test_runner(browser, headless):
    test = TestTc1()
    test.setup_method(method=None, browser=browser, headless=headless)
    try:
        test.test_tc1()
        screenshot_name = f"test_{browser}.png"
        test.save_screenshot(screenshot_name)
    except Exception as e:
        screenshot_name = f"error_z_{browser}.png"
        test.save_screenshot(screenshot_name)
        print(f"Zapisano zrzut ekranu z błędnym testem {screenshot_name}")
        raise e
    finally:
        test.teardown_method(method=None)
