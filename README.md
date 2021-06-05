#### NodeJS+Nacos 服务注册及发现

##### 实现思路

- Node服务通过Nacos node SDK注册到nacos上
- Java通过openFeign调用Node服务
- Node通过网关调用Java服务

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

##### 代码结构

node-nacos

​	----java 

​		----java-feign              Java服务

​	    ----java-gateway        网关

​	----node                          nodejs

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

6. 验证效果

   ```html
   curl http://localhost:8282/feign/hello
   ```

   

