from selenium_framework.framework.base.base_page import BasePage
from selenium_framework.framework.elements.button import Button
from selenium_framework.framework.elements.input import Input
from selenium_framework.framework.elements.label import Label
from selenium_framework.framework.elements.table import Table
from selenium_framework.framework.logger.custom_logger import Logger
from selenium.webdriver.common.by import By
from selenium_framework.utils.make_list_from_web_list import make_list


class WebTablePage(BasePage):
    PAGE_TAG = (
        By.XPATH, '//*[contains(@class, "main-header")\
         and text()="Web Tables"]'
    )
    TABLE = (By.XPATH, '//*[@id="app"]//*[contains(@class, "rt-tbody")]')
    ADD_BTN = (By.XPATH, '//*[@id="addNewRecordButton"]')
    REGISTR_FORM_TAG = (By.XPATH, '//*[@id="registration-form-modal"]')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME_FILD = (By.XPATH, '//*[@id="lastName"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="userEmail"]')
    AGE_FIELD = (By.XPATH, '//*[@id="age"]')
    SALARY_FIELD = (By.XPATH, '//*[@id="salary"]')
    DEPARTMENT_FIELD = (By.XPATH, '//*[@id="department"]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="submit"]')
    DELETE_US_BTN = (By.XPATH, '//*[@id="delete-record-4"]')

    def click_add_btn(self):
        Logger().get_log().info("Clicking ADD_BTN")
        Button(self.ADD_BTN, "add_btn").click()

    def get_name_regist_form(self):
        Logger().get_log().info('Getting text from REGISTR_FORM')
        label = Label(
            self.REGISTR_FORM_TAG,
            "name_registr_form"
        ).get_label_text()
        return label

    def fill_the_form(self, user):
        Logger().get_log().info('Filling REGISTR_FORM')
        Input(
            self.FIRST_NAME_FIELD, "first_name_fild"
        ).send_text(user.first_name)
        Input(self.LAST_NAME_FILD, "last_name").send_text(user.last_name)
        Input(self.EMAIL_FIELD, "email").send_text(user.email)
        Input(self.AGE_FIELD, "age").send_text(user.age)
        Input(self.SALARY_FIELD, "salary").send_text(user.salary)
        Input(self.DEPARTMENT_FIELD, "department").send_text(user.department)

    def click_submit_bnt(self):
        Logger().get_log().info("Clicking SUBMIT_BTN")
        Button(self.SUBMIT_BTN, "submit_btn").click()

    def click_del_btn_user1(self):
        Logger().get_log().info("Clicking DELETE_US_BTN")
        Button(self.DELETE_US_BTN, "delete_btn").click()

    def quantity_of_records(self):
        Logger().get_log().info("Check table size")
        web_el_list = Table(self.TABLE, "table_size").list_elements()
        list_el = make_list(web_el_list)
        return len(list_el)
