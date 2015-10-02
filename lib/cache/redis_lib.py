#coding=utf8
__author__ = 'guozhiwei'
'''
    from cache.redis_lib import RedisForCluster
    conn = RedisForCluster.get_cluster_redis()
    print conn.get("guozhiwei")
    print conn.get("guozhiwei2")

'''
from rediscluster import StrictRedisCluster
import redis

class RedisForCluster:
    '''
        redis 集群客户端  单例
    '''

    INSTANCE = None

    @staticmethod
    def get_instance(flag=None):
        if not RedisForCluster.INSTANCE:
            import config
            from config import GLOBAL_CONFIG
            init_config = GLOBAL_CONFIG.get('cache').get("cluster_redis")
            RedisForCluster.INSTANCE = RedisForCluster(**init_config)
        return RedisForCluster.INSTANCE


    def __init__(self, **init_config):
        init_config['decode_responses'] = True
        self.redis_conn = StrictRedisCluster(**init_config)


    def get_connection(self):
        return self.redis_conn


    @staticmethod
    def get_cluster_redis():
        return RedisForCluster.get_instance("cluster_redis").get_connection()


class RedisForCommon:
    '''
        非集群的redis
    '''

    INSTANCE = None

    def __init__(self, **init_config):
        host = init_config.get("host")
        port = int(init_config.get('port'))
        max_connections = int(init_config.get('max_connections',20))
        pool = redis.ConnectionPool(host=host,port=port,max_connections=max_connections)
        self.redis = redis.Redis(connection_pool=pool)


    @classmethod
    def get_instance(cls, name):
        if not RedisForCommon.INSTANCE:
            import config
            from config import GLOBAL_CONFIG
            init_config = GLOBAL_CONFIG.get('cache').get(name)
            RedisForCommon.INSTANCE = RedisForCommon(**init_config)
        return RedisForCommon.INSTANCE



    @classmethod
    def get_instance_for_common_1(cls):
        return RedisForCommon.get_instance("common_redis_1").redis
