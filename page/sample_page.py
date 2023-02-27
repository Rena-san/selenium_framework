from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By


class SamplePage(BasePage):
    PAGE_TAG = (By.XPATH, '//*[@id="sampleHeading"]')

