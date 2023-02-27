from selenium_framework.framework.base.base_page import BasePage
from selenium_framework.framework.driver_utils.browser import Browser
from selenium_framework.framework.elements.label import Label
from selenium_framework.framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class FramePage(BasePage):
    PAGE_TAG = (
        By.XPATH, '//*[contains(@class, "main-header") and text()="Frames"]'
    )
    FRAME_BIG = (By.XPATH, '//*[@id="frame1Wrapper"]//*[@id="frame1"]')
    TEXT_FR_BIG = (By.XPATH, '//*[@id="sampleHeading"]')
    FRAME_SMALL = (By.XPATH, '//*[@id="frame2Wrapper"]//*[@id="frame2"]')
    TEXT_FR_SMALL = (By.XPATH, '//*[@id="sampleHeading"]')
    BROWSER_WIND_BTN = (
        By.XPATH, '//*[@class="element-list collapse show"]//*[@id="item-0"]'
    )

    def switch_to_big_frame(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_frame(FramePage.FRAME_BIG)

    def get_text_big_frame(self):
        Logger().get_log().info("Getting text from frame")
        frame_text = Label(self.TEXT_FR_BIG, "text_big_fr").get_label_text()
        return frame_text

    def fr_switch_to_default_content(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_default_content()

    def switch_to_small_frame(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_frame(FramePage.FRAME_SMALL)

    def get_text_small_frame(self):
        Logger().get_log().info("Getting text from frame")
        frame_text_s = Label(
            self.TEXT_FR_SMALL,
            "text_small_fr"
        ).get_label_text()
        return frame_text_s
