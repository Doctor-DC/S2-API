# django-api
# django 部署centos

移植静态文件配置，这个主要是将原项目的静态文件移植出来以便访问。如下，注意括号中第二个参数为移植后的目录，不要和之前的静态文件目录相同就好。

```STATIC_ROOT = os.path.join(BASE_DIR, "/var/www/static")```  

进行静态文件移植
        
        python manage.py collectstatic
  
获取依赖  
        pip freeze > requirements.txt

django项目下配置文件

    [uwsgi]
    http = 0.0.0.0:8000
    chdir = /root/python/work/venv/s2/
    wsgi-file = quickstart/wsgi.py
    master = true
    processes = 4   
    #指定静态文件
    static-map=/static=/root/python/work/venv/s2/static/ 
    stats=/root/python/work/venv/s2/uwsgi/uwsgi.status           

    pidfile=/root/python/work/venv/s2/uwsgi/uwsgi.pid

    daemonize =/root/python/work/venv/s2/uwsgi/web_uwsgi.log 


进入虚拟环境

    cd venv/  
        source bin/activate  
    cd django项目
    (pip install -r requirements.txt)


退出虚拟环境：
    
    deactivate

`启动`： `uwsgi --ini uwsgi.ini `  
停止：`uwsgi --stop uwsgi.pid `  
重启：`uwsgi --reload uwsgi.pid `  
强制停止：`killall -9 uwsgi `  

查看端口调用  
        `netstat -lnp|grep 8001`  
        `ps 进程号`    
杀掉进程    
         `kill -9 进程号`  
         
参考  
(https://www.cnblogs.com/zhming26/p/6163952.html?utm_source=itdadao&utm_medium=referral)    




# django 部署docker (无uwsgi)  

  Dockerfile 

        FROM python:3.6.5
        RUN mkdir /s2run
        WORKDIR /s2run
        COPY . /s2run
        RUN pip install --upgrade pip && \     
        pip install -r requirements.txt 

        # CMD ["/bin/bash","run.sh"]
        # RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt  
   
   docker-compose.yam
   
        django:
        container_name: django
        image: dctest:latest
        # build: .
         command: python manage.py runserver 0.0.0.0:8000
         # command: uwsgi --ini uwsgi.ini
         ports:
        - "8000:8000"
         volumes:
         - .:/code
     
   
   运行 创建容器  
        
        docker run -i -t dctest:latest

   启动容器  
   
        docker-compose up
        
 
