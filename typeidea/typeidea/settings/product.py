from .base import *  # NOQA

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '2658@sanlo',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

ADMINS = MANAGERS = (
    ('sanlozhang', '940072028@qq.com')
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')
