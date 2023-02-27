from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    PAGE_TAG = (By.XPATH, '//*[@class="home-content"]')
    ALERT_FRAME_WIND_BTN = (
        By.XPATH, '//*[@id="app"]//*[text()="Alerts, Frame & Windows"]'
    )
    ELEMENTS_BTN = (
        By.XPATH, '//*[@id="app"]//*[contains(@class, "card mt-4 top-card")]'
    )

    def click_alerts_frame_window_btn(self):
        Logger().get_log().info("Clicking ALERT_FRAME_WIND_BTN")
        Button(self.ALERT_FRAME_WIND_BTN, "alert_frame_win_btn").click()

    def click_elements_btn(self):
        Logger().get_log().info("Clicking ELEMENTS_BTN")
        Button(self.ELEMENTS_BTN, "elements_btn").click()
