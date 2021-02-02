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
SITENAME = u'Beneath Data'
SITESUBTITLE = u"A blog dedicated to data analytics and good-looking graphs."
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

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
LINKS = (
        ('FiveThirtyEight', 'http://FiveThirtyEight.com'),
        ('What If?', 'http://what-if.xkcd.com/'),
        ('McSweeney\'s', 'http://www.mcsweeneys.net/'),
        ('Fangraphs', 'http://www.fangraphs.com/'),
        ('IPython', 'http://ipython.org'),
         )

# Social widget
SOCIAL = (('github', 'http://github.com/tyleha'),
         ('twitter', 'https://twitter.com/tylerhartley'),
         ('linkedin', 'http://linkedin.com/in/tylerhartley'),
         ('google+', 'https://plus.google.com/102425100151107773886/posts'),
          ('professional site', 'http://tylerhartley.com'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css', 'extra/href_scroll.js', 'extra/jquery.zoom.js']
EXTRA_PATH_METADATA = {'extra/custom.css':{'path':'static/custom.css'},
                    'extra/href_scroll.js':{'path':'theme/js/href_scroll.js'},
                    'extra/jquery.zoom.js':{'path':'theme/js/jquery.zoom.js'},
                       }
for k in EXTRA_PATH_METADATA.keys(): # Fix backslash paths to resources if on Windows
    EXTRA_PATH_METADATA[system_path(k)] = EXTRA_PATH_METADATA.pop(k)


##################### Exterior Services ############################
DISQUS_SITENAME = 'beneathdata'
DISQUS_SHORTNAME = 'beneathdata'
DISQUS_DISPLAY_COUNTS = True

#GOOGLE_ANALYTICS = "UA-54524020-1"

ADDTHIS_PROFILE = 'ra-5420884b27b877bf'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False


####################### Theme-Specific Settings #########################
THEME = 'pelican-bootstrap3'#'html5-dopetrope'

# Pelican Theme-Specific Variables
BOOTSTRAP_THEME = 'cosmo'#'sandstone'#'lumen'
SHOW_ARTICLE_CATEGORY = True

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'

ABOUT_ME = "I'm a programmer and engineer with a love for Python. I enjoy testing odd hypotheses, investigating datasets, and creating rad graphs.\
<p>Find out more about me at <strong><a href=\"http://tylerhartley.com\" title=\"Professional Website\">tylerhartley.com</a></strong></p>\
<p>You can also contact me " + """<a href="http://www.google.com/recaptcha/mailhide/d?k=01viQ7or9YI4gJ8hto_vDniA==&amp;c=PFSG4q4HL4celXjwzCtAo6YzW_WP9gWcjNfpI6f3Gxw=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\07501viQ7or9YI4gJ8hto_vDniA\75\75\46c\75PFSG4q4HL4celXjwzCtAo6YzW_WP9gWcjNfpI6f3Gxw\075', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address"><strong>here</strong></a></p>"""
AVATAR = "/images/headshot.png"

BANNER = "/images/banner.png"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

PYGMENTS_STYLE = 'monokai'

############################ Plugins ######################################
PLUGIN_PATHS = ['plugins']
PLUGINS = ['simple_footnotes']
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

# MARKDOWN = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']
