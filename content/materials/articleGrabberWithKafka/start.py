import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado
import os
from urls import url_patterns
from tornado.options import options, define
from conf import Config

sh_connection = Config()
define("port", default=sh_connection.web['port'], help="run on the given port", type=int)


class PortalSystemApplication(tornado.web.Application):
    def __init__(self):
        handlers = url_patterns
        settings = dict(
            debug=True,
            autoreload=True,
            # cookie_secret=sh_connection.auth_system['cookie_secret'],
            # xsrf_cookies=True,
            # login_url=sh_connection.packages['AUTHENTICATE_SYSTEM'] + '/user/login',
            # logout_url=sh_connection.packages['AUTHENTICATE_SYSTEM'] + '/user/logout',
            # packages=sh_connection.packages,
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static")

        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(PortalSystemApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
