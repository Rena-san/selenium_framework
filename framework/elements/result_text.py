from framework.logger.custom_logger import Logger

from .base_element import Element


class ResultText(Element):
    def get_appears_text(self):
        Logger().get_log().info("Getting text")
        return self.find_element().text

