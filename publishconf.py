#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Following items are often useful when publishing
AUTHOR = 'Pablo'
SITENAME = '#random'
SITEURL = 'https://pablospizzamiglio.github.io/random-blog'

TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'es'
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
LOCALE = ('es', 'es_AR',)

THEME = "theme"
PATH = 'content'
# PAGE_PATHS = ['pages', ]
# ARTICLE_PATHS = ['articles', ]

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
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
OUTPUT_PATH = 'output-live/'

TYPOGRIFY = True

# Disqus
DISQUS_SITENAME = 'modnar'
# GOOGLE_ANALYTICS = ""
