#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dan Vittegleo'
SITENAME = u'/dev/null'
SITEURL = 'https://www.vittegleo.com'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Blogroll
#LINKS =  (('Github', 'https://github.com/dan-v/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/dan-v'),
	  ('linkedin', 'https://www.linkedin.com/in/danvittegleo'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

FILES_TO_COPY = (('extra/favicon.ico', 'favicon.ico'),)
JINJA_EXTENSIONS = ['jinja2.ext.do']

DISQUS_SITENAME = "mydevnull"
TWITTER_USERNAME = "danvittegleo"
GOOGLE_ANALYTICS = "UA-36570985-1"
PLUS_ONE = True

THEME = "pelican-themes/whispersTheme"

