#!/usr/bin/env python
import time
import logging
import coloredlogs
from src.main.xsys.config.GlobalConfig import GlobalConfig


class Logger(object):

    config = GlobalConfig()

    def __init__(self):
        self.logger = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                          filename='{0}/{1}-runtime.log'.format(self.config.get_LogsDir(), time.time().__str__()[10:]),
                                          level=logging.DEBUG)
        coloredlogs.install(level='DEBUG', logger=self.logger)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def error(self, msg):
        self.logger.error(msg)
