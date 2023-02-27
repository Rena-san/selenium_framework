from selenium_framework.framework.base.base_page import BasePage
from selenium_framework.framework.elements.button import Button
from selenium_framework.framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    PAGE_TAG = (By.XPATH, '//*[text()="Elements"]')
    WEB_TABLE_BTN = (By.XPATH, '//*[@id="item-3"]')

    def click_web_tab_btn(self):
        Logger().get_log().info("Clicking WEB_TABLE_BTN")
        Button(self.WEB_TABLE_BTN, "web_tab_btn").click()
