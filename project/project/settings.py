"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv  # для защиты личных данных

load_dotenv()  # получить доступ к значениям переменных среды, используя os.environ:

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-51s!$gxxwy1yv6p=vwse-0xk1*ddqmgv9!b1qi+6b&+ncoku0+'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # обязательно впишите его перед админом
    'django.contrib.admin',
    'django.contrib.auth',  # обрабатывает запросы по ссылке /accounts/ (поддержка авторизации)
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',  # добавляем для работы с плоскими страницами
    'django.contrib.flatpages',  # добавляем для работы с плоскими страницами

    'new_portal',  # созданное приложение
    'django_filters',  # сторонний пакет для фильтраций
    'accounts',  # созданное приложение

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.yandex',  # поддержка входа с помощью Yandex
    'allauth.socialaccount.providers.google',  # Пример провайдера Google

    'django_apscheduler',  # пакет использует указание времени периодического выполнения задач
]

SITE_ID = 1
SITE_URL = 'http://127.0.0.1:8000'
LOGIN_URL = '/accounts/login/'  # конкретизирует адрес страницы для аутентификации

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',  # для локализации (вставляем именно сюда, именно таков порядок

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',  # для плоских страниц
    'allauth.account.middleware.AccountMiddleware',  # Добавил промежуточное программное обеспечение учетной записи:

    'new_portal.middlewares.TimezoneMiddleware',  # для обработки часовых поясов
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # для `allauth` обязательно нужен этот процессор
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# язык, который применяется в текущий момент
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

# доступные языки для перевода
LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # для сбора всех статических файлов в папку staticfiles
STATICFILES_DIRS = [BASE_DIR / "static"]  # для подгрузки стилей из папки static

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'  # После входа, нас перебросит на страницу ЛК (index.html)
# LOGOUT_REDIRECT_URL = 'post/'                            # после выхода, перекинет по адресу(по default на стр. входа)

# Настройка бэкендов аутентификации
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # встроенный бэкенд Django реализующий аутентификацию по username;
    'allauth.account.auth_backends.AuthenticationBackend',  # бэкенд аутентификации, предоставленный пакетом allauth
]

# Настройки для django-allauth
ACCOUNT_EMAIL_REQUIRED = True  # Электронная почта обязательна для регистрации
ACCOUNT_UNIQUE_EMAIL = True  # Электронная почта должна быть уникальной
ACCOUNT_USERNAME_REQUIRED = False  # username, Имя пользователя необязательно
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Аутентификация будет выполняться по электронной почте
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Верификация электронной почты не требуется
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'                     # верификация почты обязательна
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}  # форма добавляющая юзера в группу, при регистрации
# форма добавляющая юзера в группу, при регистрации через провайдера
SOCIALACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSocialSignupForm'}
SOCIALACCOUNT_AUTO_SIGNUP = False  # Что бы класс CustomSocialSignupForm был вызван

# Настройки почты
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # для отправки писем на реальные почтовые адреса
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Для тестирования, печать писем в консоль.
EMAIL_HOST = 'smtp.yandex.ru'  # хост почтового сервера
EMAIL_PORT = 465  # порт, на который почтовый сервер принимает письма
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # пароль пользователя почтового сервера
EMAIL_USE_TLS = False  # необходимость использования TLS (зависит от почтового сервера
EMAIL_USE_SSL = True  # необходимость использования SSL (зависит от почтового сервера

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')  # почтовый адрес отправителя по умолчанию
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')  # адрес отправителя для системных уведомлений (ошибки, сбои и т.д.)

# данному списку администраторов будет приходить оповещение
ADMINS = [
    ('administrator', 'servisvlg4@mail.ru'),
]

# Если вы используете Redis Labs, то переменные CELERY_BROKER_URL и CELERY_RESULT_BACKEND должны строиться по шаблону:
# redis://логин:пароль@endpoint:port где endpoint и port вы также берёте из настроек Redis Labs.
CELERY_BROKER_URL = 'redis://localhost:6379'  # Указывает на URL брокера сообщений (Redis). По умолчанию порту 6379
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  # указывает на хранилище результатов выполнения задач
CELERY_ACCEPT_CONTENT = ['application/json']  # допустимый формат данных
CELERY_TASK_SERIALIZER = 'json'  # метод сериализация задач
CELERY_RESULT_SERIALIZER = 'json'  # метод сериализация результатов

# номера в комментариях - это пункты из итогового задания к которым относится конкретная часть кода
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},    # 1
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},  # 5 и 2
        },

    'formatters': {
        'form_debug': {
            'format': '{asctime} - [{levelname}] - {message}',
            'style': '{',
        },  # 1

        'form_warning_mail': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} ',
            'style': '{',
        },  # 1 и 5

        'form_error': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} - {exc_info} ',
            'style': '{',
        },  # 1 и 3

        'general_security_info': {
            'format': '{asctime} - [{levelname}] - {message} - {module}',
            'style': '{',
        },  # 2 и 4
    },

    'handlers': {
        'console_d': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_debug',
        },  # 1

        'console_w': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_warning_mail',
        },  # 1

        'console_e': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_error',
        },  # 1

        'general_hand': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'general.log',
        },  # 2

        'errors_hand': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'form_error',
            'filename': 'errors.log',
        },  # 3

        'security_hand': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'security.log',
        },  # 4

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'form_warning_mail',
        },  # 5
    },

    'loggers': {
        'django': {
            'handlers': ['console_d', 'console_w', 'console_e', 'general_hand', ],
            'level': 'INFO',  # TODO перед сдачей работы по модулю 28, поменять на DEBUG
            'propagate': True,
        },  # 1 и 2

        'django.request': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3 и 5

        'django.server': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3 и 5

        'django.template': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.db.backends': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.security': {
            'handlers': ['security_hand', ],
            'level': 'INFO',
            'propagate': False,
        },  # 4
    }
}

# Локализация
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
