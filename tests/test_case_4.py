import pytest
from framework.logger.custom_logger import Logger
from page.alerts_window_page import AlertsWindowPage
from page.bros_wind_page import BrowserWindowPage
from page.links_page import LinksPage
from page.main_page import MainPage
from page.sample_page import SamplePage


@pytest.mark.usefixtures("set_up")
class TestCase4:
    def test_case_4(self):
        Logger().get_log().info("Step 1")
        main_page = MainPage()
        is_mp = main_page.is_page_loaded()
        Logger().get_log().info("MainPage downloading")
        assert is_mp, "Данная страница не является MainPage."

        Logger().get_log().info("Step 2")
        main_page.click_alerts_frame_window_btn()
        alert_p = AlertsWindowPage()
        is_alert_p = alert_p.is_page_loaded()
        Logger().get_log().info("AlertsWindowPage downloading")
        assert is_alert_p, "Данная страница не является AlertWindow."
        alert_p.click_brows_window_btn()
        bw_page = BrowserWindowPage()
        is_bw = bw_page.is_page_loaded()
        Logger().get_log().info("Browser Window downloading")
        assert is_bw, "Данная страница не является Browser Window."

        Logger().get_log().info("Step 3")
        bw_page.click_new_tab_btn()
        bw_page.switch_tab()
        new_tab = SamplePage()
        new_tab.is_page_loaded()
        Logger().get_log().info("SamplePage downloading")
        assert new_tab, "Данная страница не является SamplePage."

        Logger().get_log().info("Step 4")
        bw_page.close_current_tab()

        Logger().get_log().info("Step 5")
        bw_page.click_elements_btn()
        bw_page.click_links_btn()
        links_p = LinksPage()
        is_link_p = links_p.is_page_loaded()
        Logger().get_log().info("LinksPage downloading")
        assert is_link_p, "Данная страница не является Links."

        Logger().get_log().info("Step 6")
        links_p.click_link_home()
        Logger().get_log().info("MainPage downloading")
        assert is_mp, "Данная страница не является Home."

        Logger().get_log().info("Step 7")
        links_p.switch_prev_window()
        Logger().get_log().info("LinksPage downloading")
        assert is_link_p, "Данная страница не является Links."
