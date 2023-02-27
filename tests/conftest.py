import pytest
from selenium_framework.framework.driver_utils.browser import Browser


@pytest.fixture()
def set_up():
    driver = Browser().get_driver()

    yield driver

    Browser().driver_quit(driver)

