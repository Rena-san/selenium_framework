from selenium_framework.framework.base.base_page import BasePage
from selenium_framework.framework.driver_utils.browser import Browser
from selenium_framework.framework.elements.button import Button
from selenium_framework.framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class BrowserWindowPage(BasePage):
    PAGE_TAG = (
        By.XPATH, '//*[contains(@class, "main-header")\
         and text()="Browser Windows"]'
    )
    NEW_TAB_BTN = (By.XPATH, '//*[@id="tabButton"]')
    ELEMENTS_BTN = (
        By.XPATH, '//*[@id="app"]//*[contains(@class, "element-group")]'
    )
    LINKS_BTN = (By.XPATH, '//*[@id="item-5"]')

    def click_new_tab_btn(self):
        Logger().get_log().info("Clicking NEW_TAB_BTN")
        Button(self.NEW_TAB_BTN, "new_tab_btn").click()

    def switch_tab(self):
        Logger().get_log().info("Checking tab")
        Browser().switch_next_tab()

    def close_current_tab(self):
        Logger().get_log().info("Closing tab")
        Browser().close_current_tab()

    def click_elements_btn(self):
        Logger().get_log().info("ELEMENTS_BTN")
        Button(self.ELEMENTS_BTN, "elements_btn").click()

    def click_links_btn(self):
        Logger().get_log().info("LINKS_BTN")
        Button(self.LINKS_BTN, "links_btn").click()
