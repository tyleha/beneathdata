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

########################### General Settings ###################################

AUTHOR = u'Tyler Hartley'
SITENAME = u'The Data Show'
SITESUBTITLE = u"A blog dedicated to Python, data analystics, and good-looking graphs."
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing 
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('IPython', 'http://ipython.org'),
        ('FiveThirtyEight', 'http://FiveThirtyEight.com'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/tylerhartley'),
         ('Linkedin', 'http://linkedin.com/in/tylerhartley'),
         ('Google+', 'https://plus.google.com/102425100151107773886/posts'),    
          ('My Professional Site', 'http://tylerhartley.com'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {'extra/custom.css':{'path':'static/custom.css'},
                       }
for k in EXTRA_PATH_METADATA.keys(): # Fix backslash paths to resources if on Windows
    EXTRA_PATH_METADATA[system_path(k)] = EXTRA_PATH_METADATA.pop(k)


##################### Exterior Services ############################
DISQUS_SITENAME = 'reticulatingspline'
DISQUS_SHORTNAME = 'reticulatingspline'
DISQUS_DISPLAY_COUNTS = True

GOOGLE_ANALYTICS = "UA-54524020-1"

ADDTHIS_PROFILE = 'ra-54171855518a961e'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False


####################### Theme-Specific Settings #########################
THEME = 'pelican-bootstrap3'#'html5-dopetrope'

# Pelican Theme-Specific Variables  
BOOTSTRAP_THEME = 'cosmo'#'sandstone'#'lumen'#'cosmo'
SHOW_ARTICLE_CATEGORY = True

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'

ABOUT_ME = """I'm a programmer and engineer with a love for Python. I enjoy testing odd hypotheses, investigating datasets, and building pretty good graphs."""
AVATAR = "/images/headshot.png"

BANNER = "/images/banner.png"

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

