import os
from dotenv import load_dotenv

load_dotenv()

CHANNEL_TO_REPORT = 'C051H1BCZ7U'
BOT_ID = 'D051NFYNXD5'


def get_bot_token():
    bot_token = os.getenv("SLACK_BOT_TOKEN", None)
    if bot_token is None:
        raise ValueError("can't get SLACK_BOT_TOKEN")
    return bot_token


def get_app_token():
    app_token = os.getenv("SLACK_APP_TOKEN", None)
    if app_token is None:
        raise ValueError("can't get SLACK_APP_TOKEN")
    return app_token


def get_db_uri():
    user = os.getenv('PG_USER', default='postgres')
    password = os.getenv('PG_PASS', default='password')
    host = os.getenv('PG_HOST', default='localhost')
    port = os.getenv('PG_POST', default=5432)
    db = os.getenv('PG_DB', default='')
    return f'postgresql://{user}:{password}@{host}:{port}/{db}'


def get_config():
    return {
        'channel': CHANNEL_TO_REPORT,
        'bot_id': BOT_ID,
        'app_token': get_app_token(),
        'bot_token': get_bot_token(),
        'SQLALCHEMY_DATABASE_URI': get_db_uri(),
    }
