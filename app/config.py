# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

class Config(object):
    DEBUG = False
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 8000
    HOST = 'localhost'  # чтобы сделать ссылку доступной на локальном wifi - HOST = '0.0.0.0'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}  # Правильная кодировка на русском
    # api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4} --- если использовать в самом приложении
