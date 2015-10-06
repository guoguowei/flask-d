#coding=utf8
__author__ = 'guozhiwei'
import time
import logging
import traceback
from flask import Flask
from flask.app import _request_ctx_stack
import json_helper
import log_helper
from const_define import ErrorCode
import ip_helper
import const_define

FLASK_GLOBAL_APP = None


class My_Flask(Flask):

    def dispatch_request(self):
        start_time = time.time()
        resp = super(My_Flask,self).dispatch_request()
        cost = time.time() - start_time
        req = _request_ctx_stack.top.request
        ret_data = {}
        try:
            if resp:
                resp_data = resp.data
                if resp.data.startswith("jQuery") or resp.data.startswith('jsonp'):
                    first = resp_data.find('(')
                    resp_data = resp_data[first+1:-2]
                ret_data = json_helper.loads(resp_data)
        except:
            errinfo = traceback.format_exc()
            errinfo = 'resp:%s exc:%s'%(resp,errinfo)
            log_helper.log_error( errinfo )
        ret_code = ret_data.get('code')
        if ret_code is not None:
            ret_code = int(ret_code)

        #log 不要打印password
        get_args = dict(req.args.items())
        get_args.pop('password',None)
        post_args = dict(req.form.items())
        post_args.pop('password',None)

        logging.debug("ip:%s path:%s cost:%.3fs  get args:%s post args:%s ret:%s ret_msg:%s",\
                      ip_helper.get_real_ip(req),req.full_path, cost, get_args.items(), post_args.items(), \
                      ret_code, const_define.ErrorMsg.MSG_DICT.get(ret_code))
        return resp


def get_flask_app():
    global FLASK_GLOBAL_APP
    if not FLASK_GLOBAL_APP:
        FLASK_GLOBAL_APP = My_Flask(__name__)

    FLASK_GLOBAL_APP.before_request(my_before_request)
    FLASK_GLOBAL_APP.register_error_handler(BaseException, global_error_handler)
    return FLASK_GLOBAL_APP


def global_error_handler( exception ):
    from flask import request
    errinfo = traceback.format_exc()
    errinfo = 'path:%s args:%s %s'%(request.full_path,request.values,errinfo)
    log_helper.log_error( errinfo , True)
    resp = {
        'code' : ErrorCode.SYS_ERR,
    }
    return json_helper.write(resp)


def my_before_request():
    pass


