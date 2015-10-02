#coding=utf8
__author__ = 'guozhiwei'

import config
import pymongo


mongo_instance = {}


def get_mongo_conn(flag):
    if mongo_instance.get(flag):
        return mongo_instance[flag]
    mongo_config = config.GLOBAL_CONFIG['mongo'].get(flag)
    host = mongo_config['host']
    port = int(mongo_config['port'])
    max_pool_size = mongo_config['max_pool_size']
    conn = pymongo.Connection(host=host,port=port,max_pool_size=max_pool_size)
    mongo_instance[flag] = conn
    return conn


