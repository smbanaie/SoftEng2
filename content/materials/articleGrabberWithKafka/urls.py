__author__ = 'Javad'

from handler.homeHandler import HomeHanler
from handler.searchHandler import SearchHanler
from handler.logHandler import *
url_patterns = [
    (r"/", HomeHanler, None),
    (r"/search", SearchHanler, None),
    (r"/log", LogHandler, None),
    (r"/websocket", Ws_Handler),

]