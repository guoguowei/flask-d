#coding=utf8
__author__ = 'guozhiwei'
import hashlib
import time


def md5(string):
    '''
        生成字符串的md5
    :param string:
    :return string:
    '''
    md = hashlib.md5()
    md.update(string)
    return md.hexdigest().lower()


def gen_random_session_key(key, namespace="ssj"):
    return md5('%s-%s-%s' % (key, namespace, time.time()))


def gen_token(session, app_uuid=''):
    return md5("%s-%s-%s"%(session,app_uuid,time.time()))