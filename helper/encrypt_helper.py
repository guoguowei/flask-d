#coding=utf-8
__author__ = 'guozhiwei'
'''
 加密和解密模块
 KEY必须是16字节或24字节"

    用法:
        加密:
              print encrypt('123456')
              输出  wBeB+BZ0ABg=

        解密:
              print decrypt("wBeB+BZ0ABg=")
              输出 123456

         encrypt和decrypt中的key参数可以自行更换,但是必须是16个字节或24个字节
'''

from pyDes import *
from base64 import *
import sys

def encrypt (str, key="ABCD-DBACFFF-KEY"):
    k = triple_des(key, CBC, "\0\1\2\3\4\5\6\7", pad=None, padmode=PAD_PKCS5)
    return encodestring(k.encrypt(str))[:-1]

def decrypt (str, key="ABCD-DBACFFF-KEY"):
    k = triple_des(key, CBC, "\0\1\2\3\4\5\6\7", pad=None, padmode=PAD_PKCS5)
    return k.decrypt(decodestring(str))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == '-E':
            print encrypt(sys.argv[2])
        elif sys.argv[1] == '-D':
            print decrypt(sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[1] == '-E':
            print encrypt(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == '-D':
            print decrypt(sys.argv[2], sys.argv[3])