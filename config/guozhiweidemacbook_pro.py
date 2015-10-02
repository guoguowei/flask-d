#coding=utf8
'''
    配置文件的名字 来自于主机名
    该python文件的命令 - 需要转换成  _

    用于覆盖默认的配置文件 或者自定义本主机名下面才需要的配置
'''

__author__ = 'guozhiwei'
from develop import *

TEST_VAR = 'guozhiwei_2'   #当代码运行在 guozhiweidemacbook_pro 这台主机上面的时候 这个变量覆盖了default.py中的TEST_VAR变量
