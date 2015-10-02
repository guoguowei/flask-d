#coding=utf8
'''
    注册url路由
'''
__author__ = 'guozhiwei'


import web_api.e_user.user as e_user_user


def reg(app):
    '''
        这里放外部访问的api接口
    :return:
    '''
    app.add_url_rule(rule='/ping',  view_func=e_user_user.ping, methods=['GET','POST'])



