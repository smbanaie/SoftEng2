#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
import threading
import time
import configparser

__author__ = 'J.Asoodeh, J.Salary, M.Keyvani, A.Mollaeie'


class LogToKafka(threading.Thread):
    """
        This class forwarding logs to kafka

        __init__()
            message : this variable determine message that is a part of log record
            typ : this variable determine type of message

        run()
            when thread is running run can send  message to kafka

        call_back()
            call run function again on same thread
    """

    def __init__(self, message=None, typ=None):
        super(LogToKafka, self).__init__()
        self.message = message
        self.typ = typ

    def run(self):
        # connect to kafka
        pro = KafkaProducer(bootstrap_servers='localhost:9095')

        # log record
        msg = b'{date} {type} {message}'.format(type=self.typ, date=datetime.now(), message=self.message)
        # send message to kafka
        pro.send('logs', msg)

        # waiting for 0.5 second
        time.sleep(0.5)

    def call_back(self, message=None, typ=None):
        # update message
        self.message = message
        # update typ
        self.typ = typ
        # calling run function
        self.run()


class KafkaToLogFile(threading.Thread):
    """
        This class is for picking up message from log topic and write in file
    """

    def __init__(self):
        super(KafkaToLogFile, self).__init__()
        self.settings = configparser.ConfigParser()
        self.settings.read("../config/config.ini")
        self.log = dict(self.settings.items('kafka'))
        self.msg = {}

    def run(self):
        cun = KafkaConsumer(bootstrap_servers=self.log['host'] + ':' + self.log['port'])
        cun.subscribe(['log'])
        for msg in cun:
            with open(self.log['path'], 'a') as f:
                f.write(msg.value)
            self.msg = msg.value
