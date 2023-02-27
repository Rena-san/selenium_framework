import pytest
from selenium_framework.framework.logger.custom_logger import Logger
from selenium_framework.page.alerts_window_page import AlertsWindowPage
from selenium_framework.page.frame_page import FramePage
from selenium_framework.page.main_page import MainPage
from selenium_framework.page.nested_frame_page import NestedFramePage
from selenium_framework.testing_data.read_test_data import test_text


@pytest.mark.usefixtures("set_up")
class TestCase2:
    def test_case_2(self, test_text):
        Logger().get_log().info("Step 1")
        main_page = MainPage()
        is_mp = main_page.is_page_loaded()
        Logger().get_log().info("MainPage downloading")
        assert is_mp, 'Данная страница не является main page.'

        Logger().get_log().info("Step 2")
        main_page.click_alerts_frame_window_btn()
        alert_p = AlertsWindowPage()
        is_alert_p = alert_p.is_page_loaded()
        Logger().get_log().info("AlertsWindowPage downloading")
        assert is_alert_p, 'Данная страница не является AlertWindow.'
        alert_p.click_nested_frame_btn()
        nest_fr_page = NestedFramePage()
        is_nest_p = nest_fr_page.is_page_loaded()
        Logger().get_log().info("NestedFramePage downloading")
        assert is_nest_p, 'Данная страница не является NestedFramePage.'
        nest_fr_page.switch_to_parent_frame()
        parent_fr_text = nest_fr_page.get_text_parent_frame()
        Logger().get_log().info("Check frame`s text")
        assert parent_fr_text == test_text["t2_step3_text_par_fr"], 'Текст не соответствует'
        nest_fr_page.switch_to_child_frame()
        child_fr_text = nest_fr_page.get_text_child_frame()
        Logger().get_log().info("Check frame`s text")
        assert child_fr_text == test_text["t2_step3_text_chil_fr"], 'Текст не соответствует'
        nest_fr_page.fr_switch_to_default_content()

        Logger().get_log().info("Step 3")
        nest_fr_page.click_frames_btn()
        frame_p = FramePage()
        is_fr_p = frame_p.is_page_loaded()
        Logger().get_log().info("FramePage downloading")
        assert is_fr_p, 'Данная страница не является FramePage.'
        frame_p.switch_to_big_frame()
        big_frame_text = frame_p.get_text_big_frame()
        frame_p.fr_switch_to_default_content()
        frame_p.switch_to_small_frame()
        small_frame_text = frame_p.get_text_small_frame()
        Logger().get_log().info("Check frames text")
        assert big_frame_text == small_frame_text, 'Текст фреймов не совпадает'
