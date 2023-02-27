from selenium_framework.framework.driver_utils.browser import Browser


class BasePage:

    def __init__(self):
        self.PAGE_TAG

    def is_page_loaded(self):
        return Browser().get_driver().find_element(*self.PAGE_TAG)
