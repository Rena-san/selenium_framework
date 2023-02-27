from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    @staticmethod
    def get_driver_instance(config):
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument(config["mode"])
            options.add_argument(config["language"])
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging']
            )
            driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options
            )
            driver.maximize_window()
            driver.get(config["URL"])
            driver.implicitly_wait(config["waiting_time"])
            return driver

        elif config['browser'] == 'firefox':
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install()
            )
            driver.maximize_window()
            driver.get(config["URL"])
            driver.implicitly_wait(config["waiting_time"])
            return driver
        else:
            raise Exception(f'{config["browser"]} is not a support browser')
