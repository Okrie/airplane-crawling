### -*- coding: utf8 -*-
'''
### Information
    - Created : 2024-04-25 00:00
    - Author : Okrie
    - Description : Airplane Price Information Class
    - Version : 0.1
    - License : MIT License
'''

import pandas as pd
import requests as req
import logging, logging.handlers
import os, sys
from datetime import datetime, timedelta

VERSION = 0.1
class NaverAirplane():
    """
    ## NaverAirplane Price Crawling Class by Okrie
    ---

    Args:
        

    Examples:

    >>> 
    >>> 

    """

    _logger = None
    _loggerformat = logging.Formatter('%(asctime)s %(levelname)s \t : [%(module)s]  %(message)s')

    def __init__(self):
        nowTime = datetime.now().strftime("%Y%m%d_%H")
        logFileName = f'./logs/naver_{nowTime}.log'
        datefmt = '%Y/%m/%d %I:%M:%S %p'

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(self._loggerformat)
        self._logger.addHandler(console_handler)

        loggerHandler = logging.FileHandler(filename=logFileName)
        loggerHandler.setFormatter(self._loggerformat)
        loggerHandler.setLevel(logging.DEBUG)
        self._logger.addHandler(loggerHandler)

        self.getLogger(logFileName)

    def getLogger(self, logFileName):
        """
            ## GetLogger 
            ---
            Log File name 지정을 위한 작업

            >>> 현재 날짜 기준으로 년월일_시분초
            >>> datetime.now().strftime("%Y%m%d_%H%m%S") >> 20240425_000413
            >>> f'naver_{nowTime}.log' >> naver_20240425_000413.log
        """

        # 파일 존재 유무 확인
        try:
            self._logger.debug(f'Check Log {logFileName}')
            self._logger.info(f'{logFileName} Checked')

        # 파일 존재 열 수 없을때 ERROR
        except Exception as e:
            self._logger.error(f'Can not open Logger "{logFileName}"')
            self._logger.error(f'File ERROR : {e}')
            sys.exit(1)


    