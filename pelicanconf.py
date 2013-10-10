#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Torrance'
SITENAME = u'Pravic'
SITEURL = 'http://pravic.net'

TIMEZONE = 'Pacific/Auckland'
DEFAULT_DATE_FORMAT = '%d %B %Y'

DEFAULT_LANG = u'en'

PATH='content/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN =  SITEURL
FEED_ALL_RSS = 'feeds/all.rss'

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 0

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/pravic"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

STATIC_PATHS = ['images', 'CNAME']

# Remove tags and archives from default list
DIRECT_TEMPLATES = (('index','categories'))

TYPOGRIFY = True
