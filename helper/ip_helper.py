#coding=utf8
'''
    get_real_ip(request)   #request是flask中的对象
'''
__author__ = 'guozhiwei'

def get_real_ip(request):
    ip = request.headers.get('X-Real-Ip', request.remote_addr)
    if not ip:
        ip = '9.9.9.9'
    return ip

