#coding=utf8
__author__ = 'guozhiwei'
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

