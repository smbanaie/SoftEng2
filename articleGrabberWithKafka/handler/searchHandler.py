__author__ = 'Javad'
import tornado.web


class SearchHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.render("search.html",active="search")

    def post(self, *args, **kwargs):
        pass
