#coding=utf8
__author__ = 'guozhiwei'
import os
import logging
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def init_env():
    '''
        导入sys path
    :return:
    '''
    file_basic_path = os.path.dirname(os.path.abspath(__file__))

    basic_path = file_basic_path[0:-4]
    os.environ["BASIC_PATH"] = basic_path  #basic path 放到全局的一个变量当中去
    sys.path.append( basic_path )
    sys.path.append( basic_path+'/config')
    sys.path.append( basic_path+'/helper')
    sys.path.append( basic_path+'/lib')
    sys.path.append( basic_path+'/model')
    sys.path.append( basic_path+'/interface')

init_env()

import config
from core import flask_app
from config import GLOBAL_CONFIG
from other import pid_util


def init_log(service_name):
    # 初始化log组件
    import log_helper
    logPath = GLOBAL_CONFIG.get('flask').get(service_name).get('logPath')
    logLevel = GLOBAL_CONFIG.get('flask').get(service_name).get('logLevel')
    handler = log_helper.addTimedRotatingFileHandler(logPath, service_name, logLevel = logLevel)
    return handler


def start(service_name):
    log_handler = init_log(service_name)

    flask_config = GLOBAL_CONFIG.get("flask").get(service_name)
    # 启动falsk
    options = {
        'threaded' : True,
    }
    host = flask_config.get("host")
    port = flask_config.get('port')
    debug_mode = flask_config.get('debug_mode')
    reg_module_name = flask_config.get("reg_module_name")

    #注册interface
    import reg_route
    reg_route.reg(reg_module_name)
    logging.info(" start app %s", service_name)

    #生成pid
    pidFile = os.environ["BASIC_PATH"] + '/bin/' + service_name + '_flask_app.pid'
    pid_ins = pid_util.PidUtil(service_name, pidFile)
    pid_ins.start()

    flask_app.get_flask_app().logger.addHandler(log_handler)
    flask_app.get_flask_app().run(host, port, debug_mode, **options)

    pid_ins.clear()

    logging.info('stop app %s', service_name)


def help():
    print '''
    usage:

        python main.py service_name start
        python main.py service_name stop
    '''
    sys.exit()


def stop(service_name):
    pidFile = os.environ["BASIC_PATH"] + '/bin/' + service_name + '_flask_app.pid'
    pid_ins = pid_util.PidUtil(service_name, pidFile)
    logging.info( "stop app %s", service_name )
    if pid_ins.stop() == 0:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) < 3:
        help()

    service_name = sys.argv[1]
    action = sys.argv[2]
    if action == 'start':
        start(service_name)
    elif action == 'stop':
        stop(service_name)
    else:
        help()
