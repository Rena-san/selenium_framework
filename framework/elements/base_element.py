from framework.driver_utils.browser import Browser
from framework.logger.custom_logger import Logger


class Element:

    def __init__(self, locator, name):
        self.name = name
        self.locator = locator

    def find_element(self):
        Logger().get_log().info(f"Searching element {self.name}")
        elem = Browser().get_driver().find_element(*self.locator)
        return elem

    def click(self):
        Logger().get_log().info(f"Clicking element {self.name}")
        self.find_element().click()

    def scroll_to_element(self):
        Logger().get_log().info(f"Scrolling to element {self.name}")
        scroll_to_elem = self.find_element()
        return Browser().driver.execute_script("arguments[0].scrollIntoView();", scroll_to_elem)
