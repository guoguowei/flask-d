#coding=utf8
__author__ = 'guozhiwei'
'''
    get 和 post 方法的简单封装

    #url
    #params dict  {'name':'guozhiwei',  'blog':'hiroguo.me'}
    #timeout 超时时间
    #decode_json_resp  True/False 是否需要对结果json解码
    simple_get(url, params, timeout, decode_json_resp)
    simple_post(url, params, timeout, decode_json_resp)

'''
import json_helper

import urllib
import urllib2



def simple_get(url, params={}, timeout=5, decode_json_resp=False):
    query = urllib.urlencode(params)
    if params:
        request_url = '%s?%s' % (url, query)
    else:
        request_url = url
    request = urllib2.Request(request_url)
    resp_data = urllib2.urlopen(request, timeout=timeout).read()
    if decode_json_resp:
        return json_helper.loads(resp_data)
    return resp_data



def simple_post(url, params={}, timeout=5, decode_json_resp=False):
    query = urllib.urlencode(params)
    request = urllib2.Request(url, query)
    data = urllib2.urlopen(request, timeout=timeout).read()
    if decode_json_resp:
        return json_helper.loads(data)
    return data

