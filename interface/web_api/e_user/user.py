#coding=utf8
'''
'''

__author__ = 'guozhiwei'

import const_define
from flask import request
import json_helper

def ping():
    return json_helper.format_api_resp()
