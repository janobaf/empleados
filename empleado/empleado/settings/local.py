from .base import *
DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'NAME': 'pagina',
        'ENGINE': "sql_server.pyodbc",
        'HOST':'DESKTOP-AANJO59\SQLEXPRESS',
        'USER': 'janobaf2',
        'PASSWORD': '00247887',
        'OPTIONS':{
                'driver': 'ODBC Driver 13 for SQL Server',
                
             },
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS=[BASE_DIR.child('static')]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')