from framework.driver_utils.browser_factory import BrowserFactory
from framework.singleton.singleton import Singleton
from tests.read_config import config


class Browser(metaclass=Singleton):
    driver = None

    def __init__(self):
        self.driver = BrowserFactory.get_driver_instance(config())

    def get_driver(self):
        return self.driver

    @staticmethod
    def driver_quit(driver):
        Singleton._instances = {}
        driver.quit()

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    def enter_text_to_alert_window(self, text):
        alert = self.switch_to_alert()
        alert.send_keys(text)

    def get_text_from_alert(self):
        alert_text = self.switch_to_alert().text
        return alert_text

    def switch_to_frame(self, locator):
        frame = self.driver.find_element(*locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close_current_tab(self):
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.close()
        self.driver.switch_to.window(window_before)

    def switch_previous_tab(self):
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)

    def switch_next_tab(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
