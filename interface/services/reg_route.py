#coding=utf8

from services.i_util import rate_limit

def reg(app):
    '''
    '''

    ##### example  ####
    app.add_url_rule(rule='/rate_limit',  view_func=rate_limit.rate_limit, methods=['POST','GET'])
