# flask-d
    [github](https://github.com/guoguowei/flask-d)
	flask框架的二次封装,更加方便的添加接口,能启动多个服务,并提供常用的组件

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
	

	
    
   
                   
