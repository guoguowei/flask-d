#coding=utf8
__author__ = 'guozhiwei'


GLOBAL_CONFIG = {
    'db':{
            'user' : {
                        'db_type' : 'mysql',
                        'maxconnections' : 30,  #允许的最大连接数,
                        'user' : 'test_user',
                        'passwd' : 's5IQABSd8G4=',
                        'host' : '127.0.0.1',
                        'port' : 3306,
                        'charset' : 'utf8',   #不指定的话,默认utf8
                        'database_name' : 'test_db_nmae' #数据库的名字
                    },
            'goods' : {
                        'db_type' : 'mysql',
                        'maxconnections' : 30,  #允许的最大连接数,
                        'user' : 'test_user_2',
                        'passwd' : 's5IQABSd8G4=',
                        'host' : '127.0.0.1',
                        'port' : 3306,
                        'charset' : 'utf8',   #不指定的话,默认utf8
                        'database_name' : 'test_db_name2', #数据库的名字
                    },
    },
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
    'flask' : {
        'all_services_0' : {
            'host' : '0.0.0.0',
            'port' : 19400,
            #只有开发环境和测试环境才开启debug模式  线上环境一般情况不要开启该选项 不需要的话请去掉该项
            #开启debug模式之后 代码修改之后会自动加载  不需要重启应用程序
            'debug_mode' : False,
            'reg_module_name' : 'all_services',   #这里对应reg_route文件中的相关名字
            'logLevel' : 'DEBUG',
            'logPath' : './all_services_0.log'
        },
        'all_services_1' : {
            'host' : '0.0.0.0',
            'port' : 19399,
            #只有开发环境和测试环境才开启debug模式  线上环境一般情况不要开启该选项 不需要的话请去掉该项
            #开启debug模式之后 代码修改之后会自动加载  不需要重启应用程序
            'debug_mode' : False,
            'reg_module_name' : 'all_services',   #这里对应reg_route文件中的相关名字
            'logLevel' : 'DEBUG',
            'logPath' : './all_services_1.log'
        },
        'api_web_0' : {
            'host' : '0.0.0.0',
            'port' : 19401,
            #只有开发环境和测试环境才开启debug模式  线上环境一般情况不要开启该选项 不需要的话请去掉该项
            #开启debug模式之后 代码修改之后会自动加载  不需要重启应用程序
            'debug_mode' : False,
            'reg_module_name' : 'web_api',   #这里对应reg_route文件中的相关名字
            'logLevel' : 'DEBUG',
            'logPath' : './api_web_0.log'

        },
    },
    'mongo' : {
        'suika' : {
            'host' : '127.0.0.1',
            'port' : '21000',
            'max_pool_size' : 50,
        },
    }
}
TEST_VAR = 'guozhiwei_1'




