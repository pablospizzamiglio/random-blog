#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pablo'
SITENAME = '#random'
SITEURL = ''

TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'es'
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
LOCALE = ('es', 'es_AR',)

THEME = "theme"
TYPOGRIFY = True

PATH = 'content'
# PAGE_PATHS = ['pages', ]
# ARTICLE_PATHS = ['articles', ]

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/lzzpablo'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Delete the output directory before generating new files
DELETE_OUTPUT_DIRECTORY = True

# Disqus
DISQUS_SITENAME = 'modnar'
