# flask-d
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
    
   
                   
