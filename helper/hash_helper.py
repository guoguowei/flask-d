#coding=utf8
__author__ = 'guozhiwei'

import hashlib

def sha1(string):
    sha1obj = hashlib.sha1()
    sha1obj.update(string)
    hash = sha1obj.hexdigest()
    return hash
