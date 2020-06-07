import tornado.web
from pycket.session import SessionMiXin

class BaseHandler(tornado.web.RequestHandler, SessionMiXin):
    def get_current_user(self):
        # return self.get_secret_cookie('mycookie')
        return self.session.get('mycookie')


class IndexHandler(BaseHandler):     
    def prepare(self):
        pass

    @tornado.web.authenticated
    # 如果请求方法带有装饰器并且用户没有登录, 用户会被重定向到 login_url.
    def get(self):
        # self.write("Hello World!")
        print(self.current_user)
        # self.write(HTML_TEMPLATE.format('Hello World!'))
        self.render('index.html', username=self.current_user)


class TemplateHandler(BaseHandler):
    def get(self):
        self.write('templates page')
        # self.render('index.html')
        # name = self.get_argument('name', '')
        # atag = '''
        # <a href="http://www.qq.com"> __QQ__</a><br>'''
        # self.render('02template.html', username=name, atag=atag)

    def post(self):
        name = self.get_argument('name', '')
        self.render('02template.html', username=name)


from hashlib import md5
SALT = 'tor'
def hash(text):
    return md5('{}{}'.format(text, SALT).encode()).hexdigest()
USER_DATA = {
    'gcc': hash(''),
    'qq': hash('qq'),
}
def auth(username, password):
    hash_user_pass = USER_DATA.get(username, '')
    if hash_user_pass and username and password:
        res = (hash(password) == hash_user_pass)
    else:
        res = False
    return res


class SubHandler(BaseHandler):
    def get(self):
        # 设置 cookie
        # if not self.get_cookie('mycookie'):
        #     self.set_cookie('mycookie', 'myvalue')
        #     self.write('your cookie was not set yet!')
        # else:
        #     self.write('your cookie was set!')


        # 使用 cookie_secret
        # if not self.get_secure_cookie('mycookie'):
        #     username = None
        # else:
        #     username = self.get_secure_cookie('mycookie', None)

        # 重新登录之后跳转回原来的url.
        next_url = self.get_argument('next_url', '')

        # msg = self.get_argument('msg', '')
        # self.render('submit.html', username=username, msg=msg, next_url=next_url)

    def post(self):
        # email = self.get_query_argument('email', None)
        username = self.get_body_argument('username', None)
        password = self.get_argument('password', None)
        if auth(username, password):
            self.set_secure_cookie('mycookie', username)
            next_url = self.get_argument('next_url', '/')
            self.redirect(next_url)
        else:
            self.redirect('/sub?msg={}'.format('username or password error'))