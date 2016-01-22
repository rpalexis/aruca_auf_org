# -*- coding: utf-8 -*-
import os
import socket
from django.utils.translation import gettext_lazy as _
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as \
        DEFAULT_TEMPLATE_CONTEXT_PROCESSORS
from django.conf.global_settings import MIDDLEWARE_CLASSES as \
        DEFAULT_MIDDLEWARE_CLASSES
from django.conf.global_settings import AUTHENTICATION_BACKENDS as \
        DEFAULT_AUTHENTICATION_BACKENDS

# Rapports d'erreurs
EMAIL_SUBJECT_PREFIX = '[AnnuaireRechercheBC - %s] ' % socket.gethostname()

TIME_ZONE = 'America/Montreal'
LANGUAGE_CODE = 'fr-ca'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('fr', _('Francais')),
    ('es', _('Espagnol')),
)
DEFAULT_LANGUAGE = 1

PROJECT_ROOT = os.path.dirname(__file__)
SITE_ROOT = os.path.dirname(PROJECT_ROOT)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'sitestatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = (
    'filebrowser',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'south',
    'raven.contrib.django',
    'annuaire',
    'auf.django.references',
    'diaporama',
    'appels',
    'contact',
    'photos',
    'sekizai',
    'south',
    'pagination',
    #'tinymce',
    'cms',
    'mptt',
    'menus',
    'cms.plugins.text',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'diaporama.context_processors.list_slider',
    'djangoflash.context_processors.flash',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
)

#TEMPLATE_LOADERS = (
#    'admin_tools.template_loaders.Loader',
#)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auf.django.piwik.middleware.TrackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'annuaire.middleware.ChercheurMiddleware',
    'djangoflash.middleware.FlashMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'authentification.PersonneBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/connexion/'
LOGIN_REDIRECT_URL = '/chercheur/perso/'


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    os.path.join(os.path.dirname(__file__), "annuaire/templates"),
)

CMS_TEMPLATES = (
        ('page.html', ('Page Texte')),
)

SOUTH_TESTS_MIGRATE = False

ADMIN_TOOLS_INDEX_DASHBOARD = 'project.dashboard.CustomIndexDashboard'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'dynamo': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

from conf import *

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_buttons1' : "formatselect,|,bold,italic,underline,|,bullist,numlist,|,undo,redo,|,link,unlink,image,|,backcolor,|removeformat,visualaid,code,",
    'theme_advanced_buttons2' : "",
    'theme_advanced_buttons3' : "",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_toolbar_align' : "left",
    'width' : "800",
    'height' : "200",
    'theme_advanced_resizing' : "true",
    'custom_undo_redo_levels': 10,
    'theme_advanced_toolbar_location' : 'top',
}
