from selenium_framework.framework.base.base_page import BasePage
from selenium_framework.framework.driver_utils.browser import Browser
from selenium_framework.framework.elements.button import Button
from selenium_framework.framework.elements.result_text import ResultText
from selenium_framework.framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By
from selenium_framework.utils.random_text import generate_random_string


class AlertsPage(BasePage):
    PAGE_TAG = (By.XPATH, '//*[text()="Alerts"]')
    CLICK_ME_TO_SEE_ALERT_BTN = (
        By.XPATH, '//*[@id="javascriptAlertsWrapper"]//*[@id="alertButton"]'
    )
    CLICK_ME_TO_APPEAR_CONFIRM_BOX_BTN = (
        By.XPATH, '//*[@id="javascriptAlertsWrapper"]//*[@id="confirmButton"]'
    )
    CONFIRM_TEXT = (
        By.XPATH, '//*[@id="javascriptAlertsWrapper"]//*[@id="confirmResult"]'
    )
    CLICK_ME_TO_APPEAR_PROMPT_BOX_BTN = (
        By.XPATH, '//*[@id="javascriptAlertsWrapper"]//*[@id="promtButton"]'
    )
    PROMPT_TEXT = (
        By.XPATH, '//*[@id="javascriptAlertsWrapper"]//*[@id="promptResult"]'
    )

    def click_to_see_alert_btn(self):
        Logger().get_log().info('Clicking <click me> button to see alert')
        Button(self.CLICK_ME_TO_SEE_ALERT_BTN, 'alert_btn').click()

    def open_alert_with_text(self):
        Logger().get_log().info('Getting text from alert')
        alert_text = Browser().get_text_from_alert()
        return alert_text

    def accept_alert(self):
        Logger().get_log().info('Accepting alert')
        Browser().accept_alert()

    def click_to_see_confirm_box_btn(self):
        Logger().get_log().info('Clicking <click me> button')
        Button(
            self.CLICK_ME_TO_APPEAR_CONFIRM_BOX_BTN,
            'alert_confirm_btn'
        ).click()

    def get_text_will_appear_after_accept_confirm_alert(self):
        Logger().get_log().info('Getting text from confirm box alert')
        text = ResultText(self.CONFIRM_TEXT, 'confirm_text').get_appears_text()
        return text

    def click_to_see_prompt_box_btn(self):
        Logger().get_log().info('Clicking <click me> button')
        Button(
            self.CLICK_ME_TO_APPEAR_PROMPT_BOX_BTN,
            "alert_promptbox_btn"
        ).click()

    def send_text_to_alert(self):
        Logger().get_log().info('Sending text to prompt box alert')
        random_string = generate_random_string()
        Browser().enter_text_to_alert_window(random_string)
        return 'You entered' + ' ' + random_string

    def get_text_will_appear_after_accept_prompt_alert(self):
        Logger().get_log().info('Getting text from prompt box alert')
        prompt_box_text = ResultText(
            self.PROMPT_TEXT,
            'promptbox_text'
        ).get_appears_text()
        return prompt_box_text
