#coding=utf8
'''

    日志文件自动按照每天的日期切分

    filename log文件名 包含路径
    **kwargs  backupCount  最多保存多少天
              logLevel  可选指  DEBUG INFO ERROR WARNGING
    addTimedRotatingFileHandler(filename, **kwargs)
'''
__author__ = 'guozhiwei'
import os
import logging
import logging.handlers


def addTimedRotatingFileHandler(filename, **kwargs):
    '''
        给logger添加一个时间切换文件的handler。
        默认时间是0点开始备份。
        如果不指定logger，则使用logging.getLogger()，也就是RootLogger。
    '''
    dname = os.path.dirname(filename)
    if dname and not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    conf = {
        'when': 'midnight',
        'backupCount': kwargs.get('backupCount',30),
        'format': '[%(asctime)s][%(filename)s-L%(lineno)d][%(levelname)s]: %(message)s',
        'logger': logging.getLogger(),
    }
    conf.update(kwargs)
    if conf.has_key('logLevel'):
        if isinstance(conf['logLevel'], str):
            conf['logLevel'] = getattr(logging, conf['logLevel'])
        conf['logger'].setLevel(conf['logLevel'])
    handler = logging.handlers.TimedRotatingFileHandler(
        filename = filename,
        when = conf['when'],
        backupCount = conf['backupCount'],
    )
    handler.setFormatter(
        logging.Formatter(conf['format'])
    )
    conf['logger'].addHandler(handler)
    return handler



def log_error(trackback_err_info, is_alert = False):
    '''
    :param trackback_err_info :  这个参数请使用traceback.format_exc()  来生成错误信息
           bool is_alert    :    是否需要发送短信或者邮件告警信息
    :return:
    '''
    logging.error(trackback_err_info)
    #TODO 是否需要发送告警信息