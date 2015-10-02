## 测试框架

Description: 跑测试用例

Usage:
    python test/test.py [options]

OPTIONS:
   -h    查看帮助文档
   -i 输出请求详细（默认仅输出错误）
   -f 文件路径(默认测试全部tests文件夹下的)

sample

```bash
# 跑test/tests/下面的所有用例
python test/test.py

# 跑test/tests/下面的sample.json
python test/test.py -f sample.json

# 跑test/tests/下面的所有用例，并输出详细信息
python test/test.py -i
```

## 测试用例写法

sample
```json
{
   "host": "http://api.peiwoapi.com",
   "env": {
      "app": 1,
      "version": 163
   },
   "user": {
        "uid": 25555,
        "password": "12345678"
   },
   "tests": [
     {
        "api": "/v1.0/im/messages",
        "method": "GET",
        "params": {
        },
        "except": {
           "type": "object",
           "properties": {
              "code": {
                 "type": "number",
                 "maximum": 0
              }
           },
           "required": ["code", "data"]
        }
     },
     {
        "api": "/v1.0/setting/httpservers",
        "method": "GET",
        "params": {
        },
        "except": {
           "type": "object",
           "properties": {
              "code": {
                 "type": "number",
                 "maximum": 0
              }
           },
           "required": ["code", "data"]
        }
     }
   ]
}
```

### 说明

1. host: 需要测试的api
2. env: 需要模拟的env环境，可无
3. user: 用户的信息，有些api需要登录。有此信息是将自动登录。
4. tests: 测试用例test的数组

test的详情

| key | Requried | type | description |
|-----|----------|------|-------------|
| api | y        | string| 需要测试的api|
| method | y     | string| GET或POST|
| params | n     | object| 所要传的参数，可无|
| except | n     | object|期待的结果json schema，可无。|

