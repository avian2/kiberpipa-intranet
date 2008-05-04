# Django settings for intranet project.
import os
def next_to_this_file(this_file, additional_path):
    return os.path.join(os.path.dirname(os.path.abspath(this_file)), additional_path)


ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'sl'

SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x&@ve8lp+4g3%^hgigvuv3svcig^3jbz@&w=_e4h#vaw2#odmg'
MEDIA_ROOT = next_to_this_file(__file__, '../media')
ADMIN_MEDIA_PREFIX = '/admin-media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    #'sphene.community.middleware.ThreadLocals',
    #'sphene.community.middleware.GroupMiddleware',
    'intranet.psyco.PsycoMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'intranet.middleware.requirelogin.RequireLoginMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'intranet.stats.StatsMiddleware',
)

ROOT_URLCONF = 'intranet.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'intranet.org.context_processors.media_url',
    'intranet.org.context_processors.admin_media_prefix',
    #'sphene.community.context_processors.navigation',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'intranet.org',
    'intranet.web',
#    'intranet.k6_4',
#    'intranet.slotechart',
    'django.contrib.comments',
#    'intranet.mediarchive',
    'intranet.tags',
#    'intranet.k4',
#    'intranet.kapelica',
#    'intranet.video',
    'intranet.thumbnail',
    'intranet.wiki',
    'django.contrib.admin',
    'django.contrib.markup',
    'django_evolution',
    #'sphene.sphwiki',
    #'sphene.community',
)

TEMPLATE_DIRS = (
    #next_to_this_file(__file__, '../templates'),
    '/home/redduck666/i/svn/intranet/rd666/templates',
)

AUTH_PROFILE_MODULE = "org.UserProfile"
REQUIRE_LOGIN_PATH = '/intranet/accounts/login/'

from localsettings import *