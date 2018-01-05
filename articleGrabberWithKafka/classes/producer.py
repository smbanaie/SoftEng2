#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaProducer
import threading, time


class GetArticle(threading.Thread):
    def __init__(self, message=None):
        self.message = message
        super(GetArticle, self).__init__()

    def run(self, message=None):
        pro = KafkaProducer(bootstrap_servers='localhost:9095')
        if message is not None:
            pro.send('article', message)
        else:
            pro.send('article', self.message)

        time.sleep(0.5)

    def call_back(self, message=None):
        self.run(message=message)
