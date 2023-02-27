import pytest
from selenium_framework.framework.logger.custom_logger import Logger
from selenium_framework.page.alerts_page import AlertsPage
from selenium_framework.page.alerts_window_page import AlertsWindowPage
from selenium_framework.page.main_page import MainPage
from selenium_framework.testing_data.read_test_data import test_text


@pytest.mark.usefixtures("set_up")
class TestCase1:
    def test_case_1(self, test_text):
        Logger().get_log().info("Step 1")
        main_page = MainPage()
        is_mp = main_page.is_page_loaded()
        Logger().get_log().info("MainPage downloading")
        assert is_mp, "Данная страница не является main page."

        Logger().get_log().info("Step 2")
        main_page.click_alerts_frame_window_btn()
        alert_w_p = AlertsWindowPage()
        is_alert_w_p = alert_w_p.is_page_loaded()
        Logger().get_log().info("AlertsWindowPage downloading")
        assert is_alert_w_p, "Данная страница не является AlertWindow."
        alert_w_p.click_alerts_btn()
        alerts_p = AlertsPage()
        Logger().get_log().info("AlertsPage downloading")
        assert alerts_p, "Данная страница не является AlertWindow."

        Logger().get_log().info("Step 3")
        alerts_p.click_to_see_alert_btn()
        open_alert_with_text = alerts_p.open_alert_with_text()
        Logger().get_log().info("Check alert`s text")
        assert open_alert_with_text == test_text["t1_step3_alert_text"], (
            "Текст алерта отличается от тестовых данных"
        )

        Logger().get_log().info("Step 4")
        alerts_p.accept_alert()

        Logger().get_log().info("Step 5")
        alerts_p.click_to_see_confirm_box_btn()
        open_alert_with_text = alerts_p.open_alert_with_text()
        Logger().get_log().info("Compare alert confirm`s text with test data")
        assert open_alert_with_text == test_text["t1_step5_alert_text"], (
            "Текст алерта отличается от тестовых данных"
        )

        Logger().get_log().info("Step 6")
        alerts_p.accept_alert()
        conftext = alerts_p.get_text_will_appear_after_accept_confirm_alert()
        Logger().get_log().info("Check text which appears after confirm alert")
        assert conftext == test_text["t1_step6_appear_text"], (
            "Появившийся текст не соответствует тексту алерта"
        )

        Logger().get_log().info("Step 7")
        alerts_p.click_to_see_prompt_box_btn()
        open_alert_with_text = alerts_p.open_alert_with_text()
        Logger().get_log().info("Compare alert`s prompt text with test data")
        assert open_alert_with_text == test_text["t1_step7_alert_text"], (
            "Текст алерта отличается от тестовых данных"
        )

        Logger().get_log().info("Step 8")
        sent_text = alerts_p.send_text_to_alert()
        alerts_p.accept_alert()
        prompt_text = alerts_p.get_text_will_appear_after_accept_prompt_alert()
        Logger().get_log().info(
            "Check text which appears after confirm prompt alert"
        )
        assert sent_text == prompt_text, (
            "Текст не соответствует введеному в алерт")
