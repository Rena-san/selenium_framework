from selenium_framework.framework.logger.custom_logger import Logger

from .base_element import Element


class Label(Element):

    def get_label_text(self):
        Logger().get_log().info("Getting text")
        return self.find_element().text
