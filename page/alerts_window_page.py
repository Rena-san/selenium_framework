from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class AlertsWindowPage(BasePage):
    PAGE_TAG = (By.XPATH, '//*[text()="Alerts, Frame & Windows"]')
    ALERTS_BTN = (
        By.XPATH, '//*[@class="element-list collapse show"]//*[@id="item-1"]'
    )
    NESTED_FRAMES_BTN = (
        By.XPATH, '//*[@class="element-list collapse show"]//*[@id="item-3"]'
    )
    BROWSER_WIND_BTN = (
        By.XPATH, '//*[@class="element-list collapse show"]//*[@id="item-0"]'
    )

    def click_alerts_btn(self):
        Logger().get_log().info("Clicking ALERTS_BTN")
        Button(self.ALERTS_BTN, "alerts_btn").click()

    def click_nested_frame_btn(self):
        Logger().get_log().info("scrolling to and clicking NESTED_FRAMES_BTN ")
        Button(self.NESTED_FRAMES_BTN, "nested_fr_btn").scroll_to_element()
        Button(self.NESTED_FRAMES_BTN, "nested_fr_btn").click()

    def click_brows_window_btn(self):
        Logger().get_log().info("Clicking BROWSER_WIND_BTN")
        Button(self.BROWSER_WIND_BTN, "brows_win_btn").click()
