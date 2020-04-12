<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-04-11 19:25:11
 * @LastEditTime: 2020-04-11 21:12:24
 * @FilePath: /Coding-Daily/content/Nginx相关/Nginx.md
 * @description: type some description
 -->
## Nginx学习

### 简介
高性能HTTP和反向代理服务器，以运行稳定、配质检单、资源消耗低而闻名。

### 安装
ubantu Linux中使用以下安装
```
sudo apt-get install nginx
```
安装程序把Nginx以服务的形式安装在系统中，相关的程序以及文件路径如下：
- 程序文件：放在`/usr/sbin/nginx`目录中
- 全局配置文件：`/etc/nginx/nginx.conf`
- 访问日志文件：`/var/log/nginx/access.log`
- 错误日志文件：`/var/log/nginx/error.log`
- 站点配置文件：`/etc/nginx/sites-enabled/default`

安装好后可以通过如下命令启动Nginx服务器：
```
sudo service nginx start
```
停止Nginx服务器：
```
sudo service nginx stop
```
查看Nginx服务的状态
```
sudo service nginx status
```

### Nginx配置文件
Nginx安装后以默认方式启动，在开发调试的过程中可能需要调整Nginx的运行参数，这些运行参数通过
全局配置文件`nginx.conf`和站点配置文件`sites-enabled/*`进行设置。
对全局配置文件`/etc/nginx/nginx.conf`中的关键可设置参数解析如下:
```
user www-data                           ## 定义运行Nginx的用户
worker_processes 4;                     ## Nginx进程数应该设置与系统cpu数量相等的数值
worker_rlimit_nofile 65535              ## 每个Nginx进程可以打开的最大文件数
events {
    worker_connections  768;            ## 每个Nginx进程允许的最大客户端连接数
    # 在Nginx连接到一个新连接通知后调用accept()来接受尽量多的连接
    multi_accept off;
}

http {
    ## Basic Settings

    sendfile on;                        ## 是否允许文件上传
    client_header_buffer_size 32k;      ## 上传文件大小限制
    tcp_nopush on;                      ## 防止网络阻塞
    tcp_nodelay on;                     ## 防止网络阻塞
    keepalive_timeout 65;               ## 允许的客户端长连接最大秒数

    ## Nginx散列表大小。本质越大，占用的内存空间越大，但路由速度越快
    types_hash_max_size 2048;

    access_log /var/log/nginx/access.log;       ## 访问日志文件路径名
    error_log /var/log/nginx/error.log;         ## 错误日志文件路径

    ## 如下两条用include命令加载站点配置文件
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```
在每个Nginx服务器中可以运行多个Web站点，每个站点的配置通过站点配置文件设置。
每个站点应该以一个单独的配置文件存放在`/etc/nginx/sites-enabled/default`
对其中键内容的解析如下：
```
server {
    ## 配置站点监听的端口
    listen 80;

    root /usr/share/nginx/html;                 ## 配置HTTP根页面目录
    index index.html index.htm;                 ## 配置HTTP根目录中的默认页面

    # 站点监听的IP地址，默认的localhost只可用于本机访问，一般需要将其更改为真实IP
    server_name localhost;

    ## location用于配置URL的转发接口
    location /user/ {
        ## 此处配置http://server_name/user/的转发地址
        proxy_pass http://127.0.0.1:8080;
    }

    ## 错误页面配置，如下配置定义HTTP 404错误的显示页面为/404.html
    error_page 404 /404.html;
}
```
### 安装uWSGI及配置










