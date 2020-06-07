"""
Django 项目相关配置
"""
from common_utils import UtilsFunction


class DjangoDeployUsages(UtilsFunction):
    def usage_contents(self):
        if self.str_choice == "Redis_cache":
            self.usage_infos = """pip install -i https://pypi.douban.com/simple django-redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}"""
            print(self.usage_infos)
        elif self.str_choice == "static":
            self.usage_infos = """
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]"""
            print(self.usage_infos)
        elif self.str_choice == "Celery":
            self.usage_infos = """Celery是一个使用Python开发的分布式任务调度模块, Celery专注于实时处理任务, 同时也支持任务的定时调度. 适合实时异步任务、定时任务等调度场景.
> > 任务队列是一种跨线程、跨机器工作的一种机制.任务队列中包含称作任务的工作单元. 有专门的工作进程持续不断的监视任务队列，并从中获得新的任务并处理.

> > Worker 是一个span独立的进程, 任务执行单元, 持续监视队列中是否有需要处理的任务.

> > Broker 是消息传输中间件, 任务调度队列. 它接收生产者发出的消息, 将任务存入队列, 然后派发给 Worker.

> > Backend 存储任务执行结果, 同消息中间件一样, 需要其它存储系统提供支持.

## Install and config

pip install celery
>> In 项目根目录下, 新建 **celery_tasks 包**, 新建 **config.py** 文件 与 **main.py** 文件.
    (In config.py)      broker_url = 'redis://url/(0-15)'
- In main.py
---为 celery 使用 Django配置文件(manage.py) 进行配置.
    import os
        if not os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault['DJANGO_SETTINGS_MODULE'] = '项目名.settings'
    
(创建 celery 实例)   app = celery('send_sms')
(导入 celery 配置)   app.config_from_object('celery_tasks.config')

---In celery_tasks 包中, 新建 包, 新建 存放任务逻辑代码的 py 文件."""
            print(self.usage_infos)
        elif self.str_choice == "Nginx":
            pass

        elif self.str_choice == "uWSGI":
            self.usage_infos = """在项目根目录下, 执行 pip3 freeze > requirements.txt 生成依赖包列表. 在环境中, 执行 pip3 install -r requirements.txt 安装依赖包.
>> 创建一个 settings 副本并命名作为项目启动文件, 设置 DEBUG = False.
>> 在 wsgi.py 文件中, os.environ.setdefault('DJANGO_SETTINGS_MODULE', '项目名.启动文件名')

---测试是否安装成功
    pip install uWSGI

    def application(env, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello World"]

    uwsgi --http :9090 --wsgi-file 文件名
    curl url:port"""
            print(self.usage_infos)


djangodeployusages = DjangoDeployUsages([{"Redis_cache": "", "Celery": "", "Nginx": "", "uWSGI": "", "static": ""}])
djangodeployusages.judge_options()
