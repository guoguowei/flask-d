#coding=utf8
'''
'''

__author__ = 'guozhiwei'

import logging
import const_define
from flask import request
import config
import json_helper

def ping():
    a = config
    logging.debug('test var %s ', config.TEST_VAR)
    return json_helper.format_api_resp()
