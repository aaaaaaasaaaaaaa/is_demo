# Пример local_settings
# Измените данные на свои

DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

TINKOFF_API_KEY = 'your-api-key'
ENDPOINT_TINKOFF = 'your-secret-key'
API_KEY_TINKOFF = 'your-api-key'
SECRET_KEY_TINKOFF = 'your-secret-key'

OPEN_AI_API_KEY = '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'
TG_KEY = '5444154975:AAGr99opTZz29NaiNDHR1K1fkUvx9ofH4Co'

NGROK_URL = 'https://gorgeous-exact-lionfish.ngrok-free.app'

APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-mbxtvt.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='is_demo',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.66d6e2fe71c4b3.09231189',
    application_bitrix_client_secret='ZIEVRAMtXuhwYBr9bd3s2Sh1bd2g9zsXm525oT7hfAIv3KgziD',
    application_index_path='/',
)

DOMAIN = "https://gorgeous-exact-lionfish.ngrok-free.app"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'foodgram',
        'USER': 'postgresql',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
