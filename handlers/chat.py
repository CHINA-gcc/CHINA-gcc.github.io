from tornado.websocket import WebSocketHandler


class ChatWSHandler(WebSocketHandler):
    """
    处理和响应 websocket 连接的
    """
    def open(self):
        """新的 WebSocket 连接打开, 自动调用."""
        print("new ws connection")

    def on_message(self, message):
        print("get message: {}".format(message))

    def on_close(self):
        print("close ws connection")