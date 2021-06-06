#### NodeJS+Python+Nacos 服务注册及发现

##### 实现思路

- Node服务通过Nacos node SDK注册到nacos上
- Java通过openFeign调用Node服务
- Node通过网关调用Java服务
- Python通过网关调用Java服务
- Node与Python互相调用通过网关即可

##### 环境

| 组件                | 版本           |
| ------------------- | -------------- |
| JDK                 | 8              |
| Nacos               | 2.0.1          |
| Springboot          | 2.3.11.RELEASE |
| SpringCloud         | Hoxton.RELEASE |
| SpringCloud Alibaba | 2.1.2.RELEASE  |
| OpenFeign           | 2.2.0.RELEASE  |
| Gateway             | 2.2.0.RELEASE  |
| Nacos Node SDK      | 2.1.1          |
| Node                | 14.17.0        |
| Python              | 3.9.5          |

##### 服务地址

| 服务         | 地址           |
| ------------ | -------------- |
| Nacos        | 127.0.0.1:8848 |
| java-feign   | 127.0.0.1:8181 |
| java-gateway | 127.0.0.1:8282 |
| nodejs       | 127.0.0.1:8080 |
| python       | 127.0.0.1:9999 |

##### 代码结构

```
node-nacos
│   README.md 
│
└───java
│   │
│   └───java-feign
│   │
│   └───java-gateway
│   
└───node
│    │   node-service.js
│    │   package.json
|    |   serviceDiscovery.js
└───python
│    │   hello.py
│    │   server.py
|    |   serviceDiscovery.py
```

##### 运行

1. 启动Nacos服务 

2. 注册Node服务

   ```javascript
   node ./node/serviceDiscovery.js
   ```

3. 启动Node服务

   ```javascript
   node ./node/node-service.js
   ```

4. 启动网关服务(java-gateway)

5. 注册Java服务(java-feign)

6. 验证NodeJs效果

   ```html
   curl http://localhost:8282/feign/nodejs/hello
   ```

7. 启动python服务

   ```python
   python ./python/server.py
   ```

8. 注册python服务

   ```python
   python ./python/serviceDiscovery.py
   ```

9. 验证python效果

   ```
   curl http://localhost:8282/feign/python/hello
   ```

##### SDK资源

[nacos-sdk-python](https://github.com/nacos-group/nacos-sdk-python)

[nacos-sdk-nodejs](https://github.com/nacos-group/nacos-sdk-nodejs)


[nacos-sdk-python]: https://github.com/nacos-group/nacos-sdk-python	"nacos-sdk-python"
[nacos-sdk-nodejs]: https://github.com/nacos-group/nacos-sdk-nodejs	"nacos-sdk-nodejs"
