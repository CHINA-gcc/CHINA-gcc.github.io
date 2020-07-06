## 路由与模板系统
- Creat a project
> cd into a directory where you'd like store your code.Then input:
```python
django-admin startproject <project_name>
```
### 路由
|schema|//host[:port#]/path/.../[?query-string](#)|
|------|------|
|schema|指定使用的协议(例如:http, https, ftp).|
|host|Http, 服务器的IP地址或者域.|
|port|端口号, http默认是80端口.|
|path|访问资源的路径.|
|query-string|发送给http服务器的数据.|
|anchor|锚点|
> First，creat views in the app_directory
```python
from django.http import HttpResponse
def index(request, pk):
    return HttpResponse("the content what's you want to display")
request is must be passed！
```
> Second, in the app/urls
```python
from django.urls import path
from . import views
app_name = 'app-name'

　urlpatterns = [
    　　　path('index/<int:pk>/<...>', views.index, kwargs={'pk': 'value1'}, name='index')
　]
```
- ① urlpatterns is a（django.urls.path and django.urls.re_path object）list.

- ② <int:pk>/ capture parameter，extra forms：<>-<>/     <>/<>/.

- ③ kwargs is a added parameter, only accept dictionary. When the key where in kwargs in accordance with the capture character's key,according to kwargs.
    **Note:If you used in the root URLconf, it will add parameter under the every path.**
- ④ name    URL 命名

### reverse、redirect
- In app/urls.py
```python
  app_name = 'app_name'
```
- In views.py
```python
  (联合 name 参数使用)
  url = reverse('app_name:name_参数')     URL 反向解析
  return redirect(url)                    URL 重定向
```
> Third, in the Project_name/urls:
```python
from django.urls import path, include

urlpatterns = [
    path('url_name/', include('app.urls')),
]
```
> 请求到来时, 首先到项目目录下的 urls.py(根URLconf模块)中查找路由规则并按顺序运行 url模式, 在第一个匹配的模式停止. 一旦匹配, Django导入并调用给定的视图. 如果中间出错或者没有匹配到, 返回404.
- re_path
正则表达式匹配的参数都会转换成字符串.
### Path Converter

- In Django, such as "<int:pk>" that is called "path converter". Here are some frequently-used  forms： 
|str|match all the character(not empty) strings except '/', This is Default type.|
|------|------|
|path|match all the character(not empty) strings, contain '/'.|
|int|match arbitrarily integers|
|slug|match arbitrarily ASCII，contain 'en dash(-)' and 'underline(_)'|
|uuid|format id|
**Template variables**
字母、数字、下划线开头, 不能以数字、下划线开头.
### 变量解析规则
> 当模板引擎在变量中遇到( . )时按照顺序进行查找: 字典键值 | 属性或方法 | 数字索引
```python
  doc = {'title': 'xx', 'items': ['coins]}
  context={'doc': doc}
```
- In templates
```python
  字典: {{ doc.items }}
  无参数函数: 直接返回结果.
```

### Templates filter
#### Syntax
```
{{ value|filter|filter }}, 底层原理为 字符串格式化.
{{ value|cut:" " }}     字符串所有空格去掉
过滤器可以使用参数.
```
**Note**: Chain call of pipline symbols. When use parameters, there should be no spaces between colons and parameters.
#### Common filters
|first|return the first element of list.|
|------|------|
|last|return the last element of list.|
|add|addition of parameters to values.|
|join|connect.|
|default|provides a default value that is used when Django is determines that the value is a false.|
|fefault_if_none| variable none uses default values.|
|capfirst|title case.|
|lower|all lowercase letters.|
|upper|all uppercase letters.|
|length|returns the length of strings and arrays.|
|length_is| whether the values of strings and arrays are specified values.|
|floatformat|floating-point formatting(reserve one decimal by default)|
|striptags|remove all HTML tags.|
|truncatechars|according to parameters given later,truncated character.|
|truncatewords|truncation in terms of words.|
|slice|cutting list.|
|date|format date and time.|
|time|formatting time|
|safe|turn off automatic escaping of variables.|
#### Custom template filters

　　A template filter specific to an app.

 Under the APP directory, creat a templatetags package.Then go to the package and creat the python module.

 APP must be registered in settings.py.

　　Custom filter is a python function.

 The first parameter is the template variable passed in.The second parameter is a default parameter which can not be written.

from django.template import Library
register = Library()

def demo_x(value, language='zh'):
　　map = {
　　　　'zh': {0: '男'，1: '女'}，
   　　'en': {0: 'male', 1: 'female'}
　　}
   return map[language][value]
register.filter('命名', demo_x)              过滤器名称也需更换.
Usage

{{% load Py文件 %}}
< label>{{ 变量|自定义过滤器}}< /label>
  Example < td>{{ student.sex|demo_x:'en'}}< /td>
Template tags
Usage

{% load static %}      加载第三方标签
{% extends '...' %}      继承模板
{% include '...'%}      全局添加(javascript)
{% for what in what %}
    <label {% if what == 'what' %}style="color: red"{% endif %}>
        <label><a href="{% url 'app_name:name属性' parameter1 parameter2 %}">{{ forloop.revcounter }}</a></label>              (模板标签 URL 反向解析)
    </label>
{% endfor %}

for representive cycle,if adding conditions,enf of endfor/endif.
forloop.counter0/forloop.revcounter positive/reverse output permutation number.
Common used labels

if/elif/else          use and/or/in/not/==/!=/<=/>= to judge. 
for..in..empty..      if there is no data, jump to empty. 
forloop.first         if it is the first iteration,return True.Otherwise false.
forloop.last          if it is last iteration,return True.Otherwise False. 
forloop.parentloop    if a nested multi-level loop is found,go back to the previous layer for.
forloop.counter | counter0 | revcounter      可以增添从 0 开始的编号.          
with                                         caching a variable.  
autoescape                                   open and close automatic escape.
comment                                      annotation.


***** All labels should use end Ending
Custom template tags

django.template.Library.simple_tag()

App 下新建 templatetags 包, 放置自定义的模板标签于 Python 模块中.
  from datetime import datetime
  from django.template import Library
  register = Library()

  @register.simple_tag(name='current', takes_context=True)
  def demo_x(context, ...):
    return  context{...}

  register.simple_tag(demo_x, name='current', takes_context=True)     ----- Register
context represents passed context variables.
 <label>{% name context内容=" " %}</label>

This custom template must be loaded into HTML.({% load ... %})

## Field
### 映射
| MySQL | ORM |
|--| ------ |
| int | IntergerField |
| varchar | CharField |
| tinyint | BooleanField |
| date | DateField(日期类型) |
|	datetime	|	DateTimeField(日期时间类型)	|
|	longtext	|	TextField	|
### 模型参数
|models.AutoField(primary_key=True)	|	指定为主键|
|:-:|:-:|
|	verbose_name|写在第一位默认verbose_name	|
|	unique|指定是否唯一(True / False)	|
|	null|	 默认为 False, 是否可以为空|
|blank	|	默认为 False, 等于True 时Form表单验证可以为空.|
|	default|	设置默认值|
|DateField.auto_now	|	每次修改都会将当前时间更新.|
|	DateField.auto_now_add| 第一次将当前时间设置进去以后不能修改.	|
二、增删改查
QuerySet(惰性) 查询集是可迭代对象, 表示数据库中对象的集合.

切片不支持负索引, 切片之后不支持附加 过滤条件 与排序.

① Append
[图片暂时无法显示]()
② Query
图片暂时无法显示
③ Update
图片暂时无法显示
④ Delete
图片暂时无法显示
Next
### 查询
模型类上的管理器(模型类.objects)来构造 QuerySet, QuerySet(惰性) 相当于 SELECT.

|filter(**kwargs)|获取一个 QuerySet, 多个条件用 and 连接.|
|:---:|:---:|
|first()|获取第一个, 返回对象.|
|last()|获取最后一个, 返回对象.|
|get(**kwargs)|获取一个对象, 如果有多个符合将报错.|
|all|获取全部, 返回 QuerySet.|
|exclude(**kwargs)|排除(与 filter 用法相同).|
|from django.db.models import Q|多条件 or 连接会用到 Q 对象.|
|value(*fields)|返回 Queryset 字典列表, 而非数据对象.|
|only(*fields)|返回 Queryset 对象列表.only 包含主键字段.|
|defer(**kwargs)|返回 Queryset (与 only 作用相反).|
|order_by(*fields)|默认升序 (ASC), <font color="red">-*fields</font> 表示 降序(DESC).|
```python
from django.db.models.functions import Lower
models_name.objects.order_by(Lower('...'))               以...小写排序
models_name.objects.order_by(Lower('...').desc())        倒序          
```
#### 聚合函数
```python
models_name.objects.aggregate(age_avg=Avg('...'))
```
> Max | from django.db.models import Max　　　　　　　最大值.
> Min | from django.db.models import Min　　　　　　　 最小值.
> Sum | from django.db.models import Sum　　　　　　　总和.
> Avg() | from django.db.models import Avg　　　　　　   平均值.

#### 分组函数
### 字段参数
> exact精确匹配 | iexact大小写不敏感
```python
model_name.objects.filter(id__exact=...)
```
> contains包含 | icontains大小写不敏感
```python
model_name.objects.filter(id__contains=...)
```
> in | 列表、元组、Queryset
```python
model_name.objects.filter(id__in=[...])
```
> gt大于 | gte大于等于
```python
model_name.objects.filter(id__gte=...)
```
> lt小于 | lte小于等于
```python
model_name.objects.filter(id__lt=[...])
```
> startswith以...开始 | istartswith大小写不敏感
```python
model_name.objects.filter(id__startswith=...)
```
> endwith以...结束 | iendwith大小写不敏感
```python
model_name.objects.filter(id__iendwith=...)
```
> range | 范围
```python
model_name.objects.filter(id__range=...)
```
> isnull | (True / False)
```python
model_name.objects.filter(id__isnull=True)
```
> contains | icontains(精确)
```python
model_name.objects.filter(id__exact)
```
### 表关系
```python
models.OneToOneField('model_name', on_delete=models.CASCADE)               级联
```
```python
models.ForeignKey('model_name', on_delete=models.SET_NULL, null=True)      一对多关系(多外键关联一, on_delete 如此设置便不影响.)
```
> 模型定义了外键, 通过外键操作.                                         正向
|model_name小写(多)_set.create('...') / add|
|---|
|model_name(多)_set.all()|
|model_name(多)_set.remove('...') / clear|
|model_name(多)_set.set([列表])		                               先执行 clear 方法|

#### 跨表查询
```python
model_name.objects.filter(相关联的字段名__其它表的字段名)
model_name.objects.filter(model_name(小写)__表的字段名)                      反向查询
```

