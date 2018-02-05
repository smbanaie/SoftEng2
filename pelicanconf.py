#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'S.Mojtaba.banaie'
SITENAME = 'Advanced Software Engineering Course Materials'
SITEURL = 'http://smbanaie.github.io/SoftwareEngineering'

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'fa'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


STATIC_PATHS = ['static', 'downloads']
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@smbanaie', 'Telegram'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
