# django-api
# django 部署centos

移植静态文件配置，这个主要是将原项目的静态文件移植出来以便访问。如下，注意括号中第二个参数为移植后的目录，不要和之前的静态文件目录相同就好。

```STATIC_ROOT = os.path.join(BASE_DIR, "/var/www/static")```  

进行静态文件移植
        
        python manage.py collectstatic

django项目下配置文件

    [uwsgi]
    http = 0.0.0.0:8000
    chdir = /root/python/work/venv/s2/
    wsgi-file = quickstart/wsgi.py
    master = true
    processes = 4   
    #指定静态文件
    static-map=/static=/root/python/work/venv/s2/static/ 


进入虚拟环境

    cd venv/
　　    source bin/activate
    cd django项目


退出虚拟环境：
    
    deactivate

启动：   `uwsgi --ini uwsgi.ini `  
停止：`uwsgi --stop uwsgi.pid `  
重启：`uwsgi --reload uwsgi.pid `  
强制停止：`killall -9 uwsgi `  
