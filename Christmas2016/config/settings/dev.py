from .base import *

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_collection')
# # print('STATIC_ROOT = ', STATIC_ROOT)
# STATIC_URL = '/c16Development/static_collection/'
