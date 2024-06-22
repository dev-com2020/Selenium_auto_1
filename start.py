from test_tc1 import TestTc1

test1 = TestTc1()
test1.setup_method(method=None, browser='chrome', headless=True)
test1.test_tc1()
test1.teardown_method(method=None)

test2 = TestTc1()
test2.setup_method(method=None, browser='firefox', headless=True)
test2.test_tc1()
test2.teardown_method(method=None)
