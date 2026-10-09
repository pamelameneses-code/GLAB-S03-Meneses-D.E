from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-tu-clave-aqui'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',
    'quiz',
    'movies',
    'news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

JAZZMIN_SETTINGS = {
    "site_title": "Administración",
    "site_header": "GLAB-S03",
    "site_brand": "Panel administrativo",
    "welcome_sign": "Bienvenido al panel",
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "news.Article": "fas fa-newspaper",
        "news.Category": "fas fa-tags",
        "news.Author": "fas fa-pen-nib",
        "quiz.Exam": "fas fa-clipboard-list",
        "quiz.Question": "fas fa-question-circle",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    "navbar": "navbar-dark navbar-navy",
    "sidebar": "sidebar-dark-navy",
    "brand_colour": "navbar-navy",
    "accent": "#2c7be5",
    "button_bg": "#2c7be5",
    "button_fg": "#ffffff",
    "sidebar_bg": "#0f172a",
    "sidebar_hover_bg": "#1d4ed8",
    "sidebar_text_color": "#e5e7eb",
    "sidebar_active_bg": "#1e3a8a",
    "sidebar_active_color": "#ffffff",
    "content_bg": "#ffffff",
    "card_bg": "#ffffff",
    "input_bg": "#ffffff",
    "input_border": "#d1d5db",
    "text_color": "#111827",
    "muted_text_color": "#6b7280",
    "table_bg": "#ffffff",
    "table_header_bg": "#f3f4f6",
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'