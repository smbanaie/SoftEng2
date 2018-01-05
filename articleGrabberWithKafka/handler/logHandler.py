# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.web
from classes.log import KafkaToLogFile
from tornado.websocket import WebSocketHandler
import json

l = []


# noinspection PyArgumentList
class LogHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("log.html",active="log")


# web socket handler
class Ws_Handler(WebSocketHandler):
    # the clients id


    # when user connection is open
    def open(self):

        # print "connection opened"

        # read message from kafka and send to client with socket
        cus = KafkaToLogFile()
        cus.start()
        message = cus.msg
        self.write_message(json.dumps({"message": message}))

    # when send message of javascript 2 python, running below function
    def on_message(self, message):
        self.write_message(u"Your message was: " + message)
        pass

    # when connection closed, running below function
    def on_close(self):
        pass
