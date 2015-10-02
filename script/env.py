#coding=utf8
__author__ = 'guozhiwei'



import sys,os

def init_env():
    '''
        导入sys path
    :return:
    '''
    # file_basic_path = /home/deploy/guozhiwei/mypy/dev-flask/bin
    file_basic_path = os.path.dirname(os.path.abspath(__file__))

    #basic_path = /home/deploy/guozhiwei/mypy/dev-flask
    basic_path = file_basic_path[0:-len('/script')]
    os.environ["BASIC_PATH"] = basic_path  #basic path 放到全局的一个变量当中去
    sys.path.append( basic_path )
    sys.path.append( basic_path+'/config')
    sys.path.append( basic_path+'/helper')
    sys.path.append( basic_path+'/lib')
    sys.path.append( basic_path+'/model')
    sys.path.append( basic_path+'/interface')
