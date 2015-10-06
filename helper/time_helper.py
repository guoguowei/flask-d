#coding=utf8
__author__ = 'guozhiwei'
import time


def get_datetime_str():
    '''
    :return:  2015-10-20 14:21:01
    '''
    return time.strftime("%Y-%m-%d %X")


def get_date_ymd_str():
    '''
    :return:  2015-10-20
    '''
    return time.strftime("%Y-%m-%d")


def get_timestamp(is_int = 1):
    '''

    :param is_int  是否需要返回整型的:
    :return  int  or float:
    '''
    ts = time.time()
    if is_int:
        ts = int(ts)
    return ts


def get_future_datetime( seconds ):
    '''
        获取未来的日期
        params  int seconds  秒数
    :return: 2015-10-11 21:11:03
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time() + seconds))


def get_before_datetime( seconds ):
    '''
        获取过去的日期
    :param int seconds: 秒数
    :return 2015-09-11 20:12:33:
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time() - seconds))


def datetime_to_str( the_datetime):
    '''
        datetime类型转换成标准格式时间字符串
    :param the_datetime:
    :return:
    '''
    return the_datetime.strftime("%Y-%m-%d %H:%M:%S")


def datetime_to_timestamp(the_datetime, is_float = False):
    '''
        datetime类型成为时间戳
    :param the_datetime:
    :return int / float:
    '''
    ms = time.mktime(the_datetime.timetuple())
    if not is_float:
        ms = int(ms)
    return ms

