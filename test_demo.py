import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """

    """
    def prepare(self):
        """

        :return:
        """
        pass

    def get(self):
        """

        :return:
        """
        self.write("Hello World!")


def make_app():
    """

    :return:
    """
    return tornado.web.Application([
        (r'/show', MainHandler),
        ],
        debug=True
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()