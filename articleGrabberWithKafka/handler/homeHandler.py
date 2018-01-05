__author__ = 'Javad'
import tornado.web


class HomeHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.render("home.html",active="home")

    def post(self, *args, **kwargs):
        pass
