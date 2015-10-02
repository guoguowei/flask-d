#coding=utf-8
__author__ = 'guozhiwei'
'''
 加密和解密模块
 KEY必须是16字节或24字节"
'''

from pyDes import *
from base64 import *
import sys

def encrypt (str, key="ABCD-DBAC-KEY"):
    k = triple_des(key, CBC, "\0\1\2\3\4\5\6\7", pad=None, padmode=PAD_PKCS5)
    return encodestring(k.encrypt(str))[:-1]

def decrypt (str, key="ABCD-DBAC-KEY"):
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