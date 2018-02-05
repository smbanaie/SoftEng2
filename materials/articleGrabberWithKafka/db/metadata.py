import configparser
from elasticsearch import Elasticsearch
import json

class MetaData:
    def __init__(self):
        self.settings = configparser.ConfigParser()
        self.settings.read("../config/config.ini")
        self.elastic = dict(self.settings.items('elastic'))
        self.es = Elasticsearch([{'host': self.elastic['host'], 'port': int(self.elastic['port'])}])