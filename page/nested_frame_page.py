from framework.base.base_page import BasePage
from framework.driver_utils.browser import Browser
from framework.elements.button import Button
from framework.elements.label import Label
from framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By


class NestedFramePage(BasePage):
    PAGE_TAG = (
        By.XPATH, '//*[contains(@class, "main-header")\
         and text()="Nested Frames"]'
    )
    PARENT_FRAME = (By.XPATH, '//*[@id="frame1Wrapper"]//*[@id="frame1"]')
    TEXT_PAR_FR = (By.XPATH, '//body')
    CHILD_FRAME = (By.XPATH, '//html/body//iframe')
    TEXT_CHILD_FR = (By.XPATH, '//body//p')
    FRAMES_BTN = (
        By.XPATH, '//*[@class="element-list collapse show"]\
        //*[@id="item-2"]'
    )

    def switch_to_parent_frame(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_frame(NestedFramePage.PARENT_FRAME)

    def get_text_parent_frame(self):
        Logger().get_log().info("Getting text from frame")
        text = Label(self.TEXT_PAR_FR, "text_pearent_fr").get_label_text()
        return text

    def switch_to_child_frame(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_frame(NestedFramePage.CHILD_FRAME)

    def get_text_child_frame(self):
        Logger().get_log().info("Getting text from frame")
        text = Label(self.TEXT_CHILD_FR, "text_child_fr").get_label_text()
        return text

    def fr_switch_to_default_content(self):
        Logger().get_log().info("Switching to frame")
        Browser().switch_to_default_content()

    def click_frames_btn(self):
        Logger().get_log().info("Clicking FRAMES_BTN")
        Button(self.FRAMES_BTN, "frames_btn").click()
