from framework.base.base_page import BasePage
from framework.driver_utils.browser import Browser
from framework.elements.link import Link
from framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class LinksPage(BasePage):
    PAGE_TAG = (
        By.XPATH, '//*[contains(@class, "main-header") and text()="Links"]'
    )
    LINK_HOME = (By.XPATH, '//*[@id="simpleLink"]')

    def click_link_home(self):
        Logger().get_log().info("Clicking LINK_HOME")
        Link(self.LINK_HOME, "link_home").find_element().click()

    def switch_prev_window(self):
        Logger().get_log().info("Switching previous tab")
        Browser().switch_previous_tab()
