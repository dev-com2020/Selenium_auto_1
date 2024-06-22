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
    finally:
        test.teardown_method(method=None)
