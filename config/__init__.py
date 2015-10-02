#coding=utf8
__author__ = 'guozhiwei'


import socket


try:
    hostname = socket.gethostname().lower()
    hostname = hostname.split('.')[0]
    exec('from %s import *' % hostname.replace('-', '_'))
except:
    from default import *
