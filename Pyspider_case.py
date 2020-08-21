## Pyspider
> Windows 系统下新建文件夹后使用 shift+鼠标右键(在此处打开命令行窗口).

### Code Logic
- 告知 scheduler on_start间隔多久执行一次.
```python
@every(minutes=24 * 60)
```
- Web 控制台点击 run 按钮时执行.
```python
def on_start(self):
```
- 调用 API 生成新的爬取任务, 任务被添加到待爬取队列.
```python
self.crawl('url', callback=self.index_page, age=..., validate_cert=False, priority=...)
```
- 告知 scheduler request的过期时间是10天, 10天内再遇到这个请求将忽略.这个参数可以在 self.crawl(url, age=10*24*60*60) 和 crawl_config 中设置.
```python
@config(age=10 * 24 * 60 * 60)
```
- 获取一个 Response 对象. response.doc 是 pyquery(类似于 jQuery 对象选择器) 对象的扩展方法.
```python
def index_page(self, response):
```
- 数字越大越先执行(优先级设置)
```python
@config(priority=2)
```
- 122
```python
def detail_page(self, response):