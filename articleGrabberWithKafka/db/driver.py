from metadata import *
from classes.log import *
from boot import log


class Article(MetaData):
    def __init__(self, text=None, record=None, id_=None):
        MetaData.__init__(self)
        self.text = text
        self.record = record
        self.id_ = id_

    def insert(self):
        try:
            self.es.index(index='articles', doc_type='article', id=self.id_, body=self.record)
        except Exception as e:
            log.call_back(message=e, typ='Error')

    def search(self):
        try:
            self.es.search(index='articles', body={
                "query":
                    {
                        "query_string":
                            {
                                "query": '{query}'.format(query=self.text)
                            }
                    }
            })
        except Exception as e:
            log.call_back(message=e, typ='Error')

# Article(record={'name':"javad"}, id_='asoo').insert()