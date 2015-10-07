# flask-d
    [github]:https://github.com/guoguowei/flask-d/
	flask框架的二次封装,更加方便的添加接口,能启动多个服务,并提供常用的组件
	
##启动
	cd bin/
	python main.py api_web_0 start
	
	#或者
	python main.py all_services_0 start
	
	api_web_0来自配置文件default.py中GLOBAL_CONFIG中的flask变量
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
    

##目录结构
###bin
    main.py   可执行文件
###config
    default.py 默认的配置文件
    develop.py 默认的开发环境配置文件,在这里能通过覆盖default.py中的变量 让开发环境拥有不同的配置
    guozhiweidemacbook_pro.py  guozhiweidemacbook_pro是我的主机名字,需要转换成小写, -替换成_ 可覆盖上面两个配置中的变量
                               如果想自定义不同的主机拥有不同的配置,可以新建一个以主机名规则的文件
###deploy
    pypi_requirement.txt  该项目依赖的外部包定义 使用pip来安装的包定义
                          pip install -r pypi_requirement.txt
###helper
    encrypt_helper.py  des加密和解密库
    hash_helper.py
    http_helper.py     封装simple_get操作和simple_post操作
    ip_helper.py       获取客户端的真实ip地址
    json_helper.py     json的read 和 write操作
                       flask返回json数据 或 jsonp数据
    log_helper.py      日志组件  可以新建每天一个log文件的日志或日志按照指定大小切割
    md5_helper.py
    regex_helper.py    常用正则封装
    time_helper.py     常用时间和日期操作封装

### interface
    web_api 不同的项目可以分不同的目录
        --reg_route   url路由文件
    services 不同的项目可以分不同的目录
        --reg_route   url路由文件
    reg_route.py  总的路由文件
    
###lib
    常用主键的类库封装
    cache
    core 对flask调用方式进行了包装
    dbs 数据库
    other
    
###model
	数据模型文件夹
### script
	脚本文件夹  跟flask没有关联,放在这里是为了能调用到config和helper和libs的代码
###test
    单元测试目录
    
    
##定义url路由
--interface
	--services
	--web_api
	
	#路由的代码
	app.add_url_rule(rule='/ping',  view_func=e_user_user.ping, methods=['GET','POST'])
	
##核心文件介绍

	--lib/core/flask_app.py   #对flask进行的简单的封装

	
	class My_Flask(Flask):
	
		#这里继承Flask,主要是想在一个总的入口的地方打印出每次请求的耗时,客户端的真实ip地址,请求的GET或POST参数
		
		
		def dispatch_request(self):
			''' 这里重写了Falsk中的该方法 '''
			#省略
			pass

	def get_flask_app():
    	global FLASK_GLOBAL_APP
    	if not FLASK_GLOBAL_APP:
        	FLASK_GLOBAL_APP = My_Flask(__name__)
		#注册每次请求之前的hook
    	FLASK_GLOBAL_APP.before_request(my_before_request)
    	#定义异常处理handler
    	FLASK_GLOBAL_APP.register_error_handler(BaseException, global_error_handler)
    	return FLASK_GLOBAL_APP			
    	
    def global_error_handler( exception ):
        #全局的错误处理handler
    	from flask import request
    	errinfo = traceback.format_exc()
    	errinfo = 'path:%s args:%s %s'%(request.full_path,request.values,errinfo)
    	log_helper.log_error( errinfo , True)
    	resp = {
        'code' : ErrorCode.SYS_ERR,
    	}
    	return json_helper.write(resp)
    	
##辅助函数介绍

###helper/encrypt_helper.py
	加密:
              print encrypt('123456')
              输出  wBeB+BZ0ABg=

    解密:
              print decrypt("wBeB+BZ0ABg=")
              输出 123456

    encrypt和decrypt中的key参数可以自行更换,但是必须是16个字节或24个字节
###helper/hash_helper.py
	计算字符串的sha1指和md5指
    
    sha1('123456')
    
    md5('123456')
###helper/http_helper.py    
	get 和 post 方法的简单封装

    #url
    #params dict  {'name':'guozhiwei',  'blog':'hiroguo.me'}
    #timeout 超时时间
    #decode_json_resp  True/False 是否需要对结果json解码
    simple_get(url, params, timeout, decode_json_resp)
    simple_post(url, params, timeout, decode_json_resp)
###helper/ip_helper.py
	get_real_ip(request)   #获取用户的真实ip地址,request是flask中的对象
###helper/log_helper.py
    日志文件自动按照每天的日期切分
    
    filename log文件名 包含路径
    **kwargs  backupCount  最多保存多少天
              logLevel  可选指  DEBUG INFO ERROR WARNGING  
    addTimedRotatingFileHandler(filename, **kwargs)

###helper/time_helper.py
	get_datetime_str()  #获取当前的日期 2015-10-20 14:21:01
	get_date_ymd_str()  #获取当前的日志 年月日 2015-10-20
	get_timestamp(is_int=1)  #return 时间戳, is_int指是1或0 表示 时间戳是否需要整形返回
	get_future_datetime(seconds) #未来的日期 seconds表示未来的多少秒 return 2015-10-11 21:11:03
	get_before_datetime(seconds) #过去的日期 seconds表示未来的多少秒 return 2015-10-11 21:11:03
	datetime_to_str(the_datetime) #datetime类型转换成标准时间字符串 2015-10-11 21:11:03
	datetime_to_timestamp(the_datetime,is_float=False) #datetime类型转换成时间戳 return int/float
	
##类库介绍
### lib/cache/redis_lib.py
	用法:
	
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
###lib/dbs/mysql.py
    使用DBUtils为MySQLDB客户端的连接池二次封装 (线程安全的)

    依赖config default.py当中的配置文件
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

    用法:
        from dbs.mysql import Mysql
        db_pool = Mysql.get_instance('goods')    #这里的goods字符串来自于上面的配置前面可key
        #从连接池中获取一个可用的连接
        db_connection = db_pool.get_connection()

        #select语句
        sql = "select * from test_table where id = %s"
        args = [222]
        res = db_pool.query(db_connection, sql, args)  #还有query_one方法

        #insert语句
        sql = "insert into test_table (name) values (%s)"
        args = ["name2"]
        #请传入刚才获取的db连接db_connection变量
        lastrowid = db_pool.insert(db_connection, sql, ['g3'])   #插入成功则返回主键id
        #请显式的提交事务  不要开启auto_commit
        db_pool.commit(db_connection)

        #update语句
        sql = "update test_table set name = %s where id = %s"
        args = ['name_333', 66]
        #请传入刚才获取的db连接db_connection变量
        db_pool.execute(db_connection, sql, args)
        #请显式的提交事务  不要开启auto_commit
        db_pool.commit(db_connection)
         
         

	

	
    
   
                   
