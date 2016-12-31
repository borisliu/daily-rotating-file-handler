import os
import logging
from dailyrotatingfilehandler import DailyRotatingFileHandler

def test_main():
    logger = logging.getLogger()
    dailyHandler = DailyRotatingFileHandler('access.log')
    logger.addHandler(dailyHandler)
    logger.setLevel(logging.DEBUG)
    logger.debug('test')
