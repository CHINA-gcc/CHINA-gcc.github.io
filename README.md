## Urllib
> Standard library for processing network requests, it consists of four models.
### urllib.request 
- Request module for initiating network requests.
- Mainly responsible for constructing and initiating network requests,and adding Headers,proxy so on.
Urlopen 方法:
```python
urllib.request.urlopen(url,data=None,[timeout]*,cafile=None,capath=None,
						cadefault=False,context=None)
```
① Urlopen recieves a string-formatted URL that sends a network request to the incoming URL and returns the  result.
```python
from urllib import request
response = request.urlopen(url='http://httpbin.org/get')
```
② By default, urlopen sends GET requests, and when Data parameters are passed in,POST requests are made.Data parameters are byte types、class files objects、iterative objects.
```python
response = request.urlopen(url='http://httpbin.org/post',
　　　　　　　　　　　　　　　　data=b'username=...&password=...')
```
③ When timeout is no specified, the system default settings are used, and timeout only works for HTTP、HTTPS、FTP connections.
```python
response = request.urlopen(url='http://httpbin.org', timeout=0.1)
```
Request 对象:
　　req = request.Request('http://httpbin.org')
　　response = request.urlopen(req)
　　


## Urllib3
### Definition
Urllib3 is a powerful and friendly HTTP client based on python3.
> Thread safety
> Connection pooling
> Client-side SSL/TLS verification
> File uploads with multipart encoding
> Helpers for retrying requests and dealing with HTTP redirects
> Support for gzip, deflate, and brotli encoding
> Proxy support for HTTP and SOCKS
> 100% test coverage

### Install
```python
pip install urllib3
```
### Construct request / Response content
```python
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')

r = http.request('POST',
　　　　　　　　　　'http://httpbin.org/post',
　　　　　　　　　　fields={'hello': 'world'})

r.status/r.data/r.headers
The HTTPResponse object provides status, data, and header attributes.
```
### Json content
```python
import urllib3
import json
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/ip')
print(json.loads(r.data.decode('utf-8')))
```
### Binary content
> The data returned by the response is of byte type, and for a large amount of data we process it by stream.
```python
http = urllib3.PoolManger()
http.request('GET', 'http://httpbin.org/bytes/1024', preload_content=False)
for chunk in r.stream(32):
　　print(chunk)
　　
More details about Streaming and IO.
```
### Proxies
```python
proxy = urllib3.ProxyManager('代理地址')
r = proxy.request('GET', 'http://httpbin.org/get')
```
### Request data
#### urllib.request 
> Add the headers parameter in dictionary format to the request method to specify the request header.
```
http = urllib3.PoolManager()
http.request('GET',
　　　　　　　　'http://httpbin.org/get',
　　　　　　　　headers={'key': 'value'}
)
print(json.loads(r,data.decode('utf-8')))
```
#### Query parameter
> GET、HEAD、DELETE, you can add query parameters by providing dictionary type parameters fields.
```python
http = urllib3.PoolManager()
r = http.request('GET',
　　　　　　　　'http://httpbin.org/get',
　　　　　　　　fields={'args': 'value'}
)
print(json.loads(r,data.decode('utf-8'))['args'])
```
> For POST and PUT, the parametes need to be encoded into the correct format through URL encoding and then spliced into the url.
```python
import urllib3
import json

from urllib.parse import urlencode

http = urllib3.PoolManager()
encoded_args = urlencode({'arg': 'value'})
url = 'http://httpbin.org/post?' + encoded_args
r = http.request('POST', url)
print(json.loads(r,data.decode('utf-8'))['args'])
```
#### Form data
> For POST and PUT, urllib3 will automatically form-encode the dictionary in the fields argument provided to request().
```python
http = urllib3.PoolManager()
r = http.request('POST',
　　　　　　　　'http://httpbin.org/post',
　　　　　　　　fields={'field': 'value'})

print(json.loads(r,data.decode('utf-8'))['form'])
```
#### Json
> When we need to send JSON data, we need to pass in the body parameter of the encoded binary data type in the request and make the request header of Content-Type. 
```python
http = urllib3.PoolManager()
data = {'attribute': 'value'}
encoded_data = json.dumps(data).encode('utf-8')
r = http.request('post',
				'http://httpbin.org/post',
				body=encoded_data,
				headers={'Content-Type': 'application/json'}
)
print(json.loads(r.data.decode('utf-8'))['json'])

访问接口我们会用到.
```
#### Files & binary data
- ①  For file upload, we can imitate the way browser forms are uploaded.
```python
with open('example.txt') as fp:
    file_data = fp.read()
r = http.request(
	'POST',
	'http://httpbin.org/post',
	fields={
		'filefield': ('example.txt', file_data)
    )}
print(json.loads(r.decode('utf-8'))['files'])
```
**爬虫一般不会用来上传文件**.
- ② For binary data upload, we specify the body and set the Content-Type request header.
```python
http = urllib3.PoolManager()
with open('example.jpg', 'rb') as fb:
    binary_data = fb.read()
r = http.request(
	'POST',
	'http://httpbin.org/post',
	body=binary_data,
    headers={'Content-Type': 'image/jpeg'}
)

print(json.loads(r.decode('utf-8')))
```
## requests
> 基于 Urllib3.
### Characteristic
Keep-Alive & 连接池 | 国际化域名和URLs | Cookie 持久性会话 | 浏览器式 SSL 验证 | 自动内容解码 基本摘要式身份认证 | 优雅的 Key/Value Cookies | 自动解压 | Unicode响应体 | HTTP(S)代理支持 分块上传 | 流下载 | 连接超时 | Chunked Requests | .netrc 支持
### 发起请求
```python
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
response = requests.put('https://httpbin.org/put', data = {'key':'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')
```
- data形式为元组列表或列表作为值的字典来完成，可以一个键对应多个值.
```python
data = {'key1': 'value1', 'key2': ['value2', 'value3']}
```
- params 参数可以允许将形如(key=value)传递给URL.
```python
headers = {} | cookies = {} |  proxies = {} | data = {} | params = {}
response = requests.get('https://httpbin.org/get', headers={}, cookies={}, 						data={}, params={'key': 'value'})

response.request.url | response.request.headers[]
     >>> https://httpbin.org/get?key1=value1&key2=value2&key2=value3
     >>> 更多细节请参见由请求猜测的文本编码 .text.
```
### 代理
```python
proxies = {'http': 'http://127.0.0.1:8888'}
```
### 重定向
```python
response = requests.get('https://httpbin.org/', allow_redirects=False)
```
### 证书验证
```python
response = requests.get('https://httpbin.org/', verify=False)
```
### 解决警告问题
```python
  from requests.packages.urllib3.exceptions import InsecureRequestWarning
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```
### 超时
```python
response = requests.get('https://httpbin.org/', timeout=...)
```
### 接收响应
- Requests发起请求获取到的是一个requests.models.Response对象.
```python
import requests
response = requests.get('https://www.gcc.xn--fiqs8s/')
```
- status_code | headers['content-type'] | encoding | text
- 可以使用 .encoding 属性找出请求正在使用的编码并进行更改.
- HTML和XML可以在正文中指定编码. 可以使用 r.content 查找编码, 然后设置 r.encoding. 这将允许您使用 r.text 正确的编码.
### 对于非文本请求
```python
from io import BytesIO
    >>> i = Image.open(BytesIO(r.content))
```
> 查看JSON数据响应内容, 建议先 r.status_code , raise_for_status()
- stream=True 你渴望得到原生的socket响应, 直接使用 Response.raw , 需要使用Response.iter_content.
```python
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
- chunk_size 自定.
- Response.iter_content 将自动解码 gzip 和 deflate 传输编码.
- Response.raw 是一个原始的字节流, 它不会转换响应内容. 如果您确实需要在返回时访问字节, 请使用 Response.raw.
- get 请求中传递timeout参数.
- 请求显式引发的所有异常都继承自 requests.exceptions.RequestException.
