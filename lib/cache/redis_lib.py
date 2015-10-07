#coding=utf8
__author__ = 'guozhiwei'
'''
    依赖与配置中的default.py
    'cache' : {
            'cluster_redis' : {
                'startup_nodes' : [      #集群的节点配置
                    {'host':'127.0.0.1','port':7000},
                    {'host':'127.0.0.1', 'port':7001},
                                ],
                'max_connections' : 50,
                'socket_timeout' : 5,   #seconds
                'socket_connect_timeout' : 5, #seconds
                'retry_on_timeout' : 5, #seconds
            },
            'common_redis_1' : {
                'host' : '127.0.0.1',
                'port' : '9000',
                'max_connections' : 50,
            }
    },


    #redis集群使用RedisForCluster类库
    #集群使用配置文件中的cluster_redis配置
    from cache.redis_lib import RedisForCluster
    conn = RedisForCluster.get_cluster_redis()
    print conn.get("guozhiwei")
    print conn.get("guozhiwei2")


    #普通redis请使用RedisForCommon
    #普通redis使用配置的common_redis_1
    conn = RedisForCommon.get_instance_for_common_1()
    print conn.set('guozhiwei','abcd')
    print conn.get('guozhiwei')


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
