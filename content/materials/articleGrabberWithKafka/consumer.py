#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import threading
from kafka import KafkaConsumer
import json
from db.driver import *


# es.get(index='sw', doc_type='people', id=2)


class Get(threading.Thread):
    def __init__(self):
        super(Get, self).__init__()

    def run(self):
        cun = KafkaConsumer(bootstrap_servers='localhost:9095')
        cun.subscribe(['article'])
        for message in cun:
            code = json.loads(message.value)['code']
            # save article in elastic
            Article(record=message.value, id_=code).insert()


if __name__ == '__main__':
    Get().start()
