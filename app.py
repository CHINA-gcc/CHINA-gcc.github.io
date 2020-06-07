import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options # 定义参数

from handlers import IndexHandler, PictureHandler, TemplateHandler, SubHandler
from handlers import chat

define('port', default='8080', help='Listening port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/temp', TemplateHandler),
            (r'/sub', SubHandler),
            (r'/ws', chat.ChatWSHandler),
        ]
        settings = dict(
            debug=True,
            static_path='static',   # 自定义目录
            static_url_prefix='/show_photo/',   # 自定义 URL 路径.
            template_path='templates',
            autoescape=None,    # 自动转义
            # cookie_secret='__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',  # 对称 key, 签名防止伪造.
            login_url='/sub',

            pycket = {
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    # 'password': '',
                    'db_session': 5,
                    # 'db_notification': 11,
                    'max_connections': 2 ** 30
                },
                'cookies': {
                    'expires_days': 30,
                }
            }
        )
        # 传入参数 settings 解包.
        super().__init__(handlers, **settings)  


# def make_app():
#     """
#
#     :return:
#     """
#     return tornado.web.Application([
#         (r'/', IndexHandler),
#         (r'/pic', PicHandler),
#     ],
#         debug=True)


if __name__ == "__main__":
    tornado.options.parse_command_line()    # 处理命令行数据后会产生 options 对象.
    app = Application()
    app.listen(options.port)
    # print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()
