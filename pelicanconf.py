#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

AUTHOR = u'Tyler Hartley'
SITENAME = u'Reticulating Spline'
SITESUBTITLE = "A blog dedicated to Python, data analystics, and good-looking graphs."
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Add custom css
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/custom.css']
EXTRA_PATH_METADATA = {system_path('extra/CNAME'):{'path':'CNAME'},
                       system_path('extra/custom.css'):{'path':'static/custom.css'},
                       }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISQUS_SITENAME = 'reticulatingspline'
DISQUS_SHORTNAME = 'reticulatingspline'
DISQUS_DISPLAY_COUNTS = True

GOOGLE_ANALYTICS = "UA-54524020-1"

ADDTHIS_PROFILE = 'ra-54171855518a961e'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
# Blogroll
LINKS = (('Python', 'http://python.org'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/tylerhartley'),
         ('Linkedin', 'http://linkedin.com/in/tylerhartley'),
         ('Google+', 'https://plus.google.com/102425100151107773886/posts'),    )

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
AVATAR = "/images/headshot.png"

BANNER = "/images/banner.jpg"

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
