from framework.driver_utils.browser import Browser
from framework.logger.custom_logger import Logger

from .base_element import Element


class Table(Element):

    def list_elements(self):
        Logger().get_log().info("Getting list of table elem.")
        list_el = Browser().driver.find_elements(*self.locator)
        return list_el


