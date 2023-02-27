import pytest
from selenium_framework.framework.logger.custom_logger import Logger
from selenium_framework.page.elements_page import ElementsPage
from selenium_framework.page.main_page import MainPage
from selenium_framework.page.web_table_page import WebTablePage
from selenium_framework.testing_data.read_test_data import test_text, user1, user2


@pytest.mark.parametrize("users", [user2(), user1()])
@pytest.mark.usefixtures("set_up")
class TestCase3:
    def test_case_3(self, users, test_text):
        Logger().get_log().info("Step 1")
        main_page = MainPage()
        is_mp = main_page.is_page_loaded()
        Logger().get_log().info("MainPage downloading")
        assert is_mp, "Данная страница не является MainPage."

        Logger().get_log().info("Step 2")
        main_page.click_elements_btn()
        el_p = ElementsPage()
        is_el_page = el_p.is_page_loaded()
        Logger().get_log().info("ElementsPage downloading")
        assert is_el_page, "Данная страница не является ElementsPage."
        el_p.click_web_tab_btn()
        web_tab_page = WebTablePage()
        is_web_tab_page = web_tab_page.is_page_loaded()
        Logger().get_log().info("WebTablePage downloading")
        assert is_web_tab_page, "Данная страница не является WebTablePage."
        table_size_before_add = web_tab_page.quantity_of_records()

        Logger().get_log().info("Step 3")
        web_tab_page.click_add_btn()
        name_form = web_tab_page.get_name_regist_form()
        Logger().get_log().info("UserForm appearing")
        assert name_form == test_text["t3_step3_name_form"], (
            "Форма отсутствует или имеет другое название"
        )
        Logger().get_log().info("Step 4")
        web_tab_page.fill_the_form(users)
        web_tab_page.click_submit_bnt()
        table_size_after_add = web_tab_page.quantity_of_records()
        Logger().get_log().info("Userinfo adding in the table")
        assert table_size_before_add < table_size_after_add, (
            "В таблицу информация не добавлена"
        )

        Logger().get_log().info("Step 5")
        web_tab_page.click_del_btn_user1()
        table_size_after_del = web_tab_page.quantity_of_records()
        Logger().get_log().info("Userinfo deleting")
        assert table_size_before_add == table_size_after_del, (
            "Запись не удалена"
        )
