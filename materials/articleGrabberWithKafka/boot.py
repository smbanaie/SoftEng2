#!usr/bib/env python
# -*- encoding UTF-8 -*-

import json
import urllib2
from classes.log import *
import configparser
import redis

from classes.crawlers import *
from classes.producer import *

if __name__ == '__main__':
    # create object log
    log = LogToKafka(typ='INFO', message='Start logging ....')
    log.start()

    # read config file
    settings = configparser.ConfigParser()
    settings.read("config/config.ini")
    rds = dict(settings.items('redis'))

    # config redis , connect to redis
    redis_ = redis.StrictRedis(host=rds['host'], port=rds['port'])

    # conference link
    link_main = 'http://www.civilica.com/ConfListing'
    r = urllib2.urlopen(link_main)
    response = r.read()

    # parsing conference page
    parser = ConferencesPage()
    parser.feed(response)

    # list of conf
    conf = parser.get_conferences_links()

    articles_main = []
    for link in conf:
        r = urllib2.urlopen('http://www.civilica.com/' + link)
        res = r.read()
        p2 = ArticlesPage()
        p2.feed(res)
        # extending
        articles_main.extend(p2.get_articles_link())

    # delete first element of array that's why is not true
    del articles_main[0]


    b = 1
    for link in articles_main:
        if b == 2:
            b = 0

        r = urllib2.urlopen('http://www.civilica.com/' + link)
        res = r.read()
        p3 = ArticleIndex()
        p3.feed(res)
        if p3.info['author']:
            code = p3.info['code']
            # check existing unique code in redis
            r = redis_.get(code)
            if r is None:
                # save in redis
                redis_.set(code, '')
                d = json.dumps(p3.info)

                # send to kafka
                if b == 1:
                    p = GetArticle(message={'data': d, 'first': True})
                    p.start()
                    log.call_back(message="article: {code} send to kafka".format(code=code),typ="success")
                    b = 2
                if b is 0:
                    p.call_back(message=d)
            else:
                log.call_back(message="article: {code} is db ".format(code=code),typ="warning")
