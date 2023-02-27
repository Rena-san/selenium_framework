import logging

from framework.singleton.singleton import Singleton


class Logger(metaclass=Singleton):
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s \t [%(levelname)s |\
             %(filename)s:%(lineno)s] > %(message)s'
        )

        console_out = logging.StreamHandler()
        console_out.setFormatter(formatter)
        self.logger.addHandler(console_out)

    def get_log(self):
        return self.logger
