from framework.logger.custom_logger import Logger

from .base_element import Element


class Input(Element):

    def send_text(self, text):
        Logger().get_log().info("Sending text to a field")
        cell = self.find_element()
        cell.send_keys(text)


