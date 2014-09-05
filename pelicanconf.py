#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tyler Hartley'
SITENAME = u'Reticulating Spline'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Python', 'http://python.org'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/tylerhartley'),
         ('Linkedin', 'http://linkedin.com/in/tylerhartley'),
		 ('Google+', 'https://plus.google.com/102425100151107773886/posts'),	)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Theme
THEME = 'pelican-bootstrap3'#'html5-dopetrope'

# Pelican Theme-Specific Variables	
BOOTSTRAP_THEME = 'cosmo'#'sandstone'#'lumen'#'cosmo'
SHOW_ARTICLE_CATEGORY = True

#SITELOGO = .png
#SITELOGO_SIZE = 
#FAVICON = .png

ABOUT_ME = """I'm a programmer and stats-head who thinks Python is fundamentally the best thing since slided bread."""# I enjoy testing odd hypotheses, investigating datasets and then building pretty graphs."""
AVATAR = "images/headshot.png"

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# Pure theme-specific variables
#COVER_IMG_URL = 'https://lh4.googleusercontent.com/-pdMEIqwnrNg/U7iV5eV_dHI/AAAAAAAARQg/H9laWRcGnpI/w1223-h905-no/IMG_20140705_201757.jpg'
#PROFILE_IMAGE_URL = 'images/headshot.png'
#TAGLINE = "Came here to fuck bitches"
