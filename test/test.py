# -*- coding: utf-8 -*-

__author__ = 'wills'

from apitester import APITester
import sys
import os
import getopt



def hashopts(pattern):
    try:
        opts, args = getopt.getopt(sys.argv[1:], pattern)
        myopts = {}
        for key, value in opts:
            myopts[key] = value or True
        return myopts
    except Exception:
        usage()


def usage():
    print '''
Description: 跑测试用例

Usage:
    python %s [options]

OPTIONS:
   -h    查看帮助文档
   -i    输出请求详细（默认仅输出错误的用例）
   -f    文件路径(默认测试全部tests文件夹下的)
''' % __file__
    sys.exit(1)

TESTPATH = './apitests'


def work():
    myopts = hashopts('hif:')
    myopts.get('-h') and usage()
    filename = myopts.get('-f')

    if filename:
        files = [filename]
    else:
        files = os.listdir(TESTPATH)

    for each in files:
        print each, ':'
        tester = APITester()
        tester.load(TESTPATH + '/' + each)
        tester.run()
        tester.summary()
        print '\n'
        if myopts.get('-i'):
            tester.report()
            print '\n'

work()
exit(0)


