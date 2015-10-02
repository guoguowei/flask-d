#coding=utf8
'''
json helper
'''
__author__ = 'guozhiwei'
import const_define
import json
from flask.ext.jsonpify import jsonify

def read(data):
    return json.loads(data)

def write(data):
    return json.dumps(data)

loads = read
dumps = write


def format_api_resp(code=0, data=None):
    resp = {
        'code' : code,
        'data' : data,
        'msg'  : const_define.ErrorMsg.MSG_DICT.get(code,''),
    }
    return jsonify(resp)