#coding=utf8
'''
    常量定义
'''
__author__ = 'guozhiwei'


class ErrorCode(object):

    SUCCESS = 0
    SYS_ERR = -10000  #系统错误
    DUPLICATED_ERR =  -10001   #重复
    PARAM_ERR = -10002 #参数错误
    CAPTCHA_ERR = -10003 #验证码错误
    EXIST_USER = -10004  #用户已经存在
    AUTH_ERROR = -10005  #权限认证错误  用户签名错误
    NOT_EXIST_USER = -10006  #用户不存在
    PWD_ERR = -10007  #密码错误
    RATE_LIMIT_ERR = -10008  #请求过于频繁

    ########################################
    MOBILE_FORMAT_ERR = -20000
    EXISTED_BIND_MOBILE = -20001

    USER_OR_PWD_ERR = -20002 #用户名或者密码错误
    THIRD_PARTY_ERR = -20003 # 第三方平台校验错误


class ErrorMsg(object):

    MSG_DICT = {
        ErrorCode.SUCCESS : 'success',
        ErrorCode.SYS_ERR : 'sys error',
        ErrorCode.DUPLICATED_ERR: 'duplicated error',
        ErrorCode.PARAM_ERR: 'param error',
        ErrorCode.CAPTCHA_ERR: 'captcha error',
        ErrorCode.EXIST_USER: 'existed user',
        ErrorCode.AUTH_ERROR: 'auth error',
        ErrorCode.NOT_EXIST_USER: 'not exist error',
        ErrorCode.PWD_ERR: 'pwd error',
        ErrorCode.RATE_LIMIT_ERR: 'rate limit error',

        ErrorCode.MOBILE_FORMAT_ERR : 'mobile error',
        ErrorCode.EXISTED_BIND_MOBILE: 'existed bind mobile',
        ErrorCode.USER_OR_PWD_ERR: 'user or pwd error',
        ErrorCode.THIRD_PARTY_ERR: 'third party auth error',
    }












