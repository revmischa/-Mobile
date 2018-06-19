import os

class Config(object):
    DEBUG = os.environ.get("DEBUG", default=False)
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql:///mm')
    SECRET_KEY = os.environ.get("SECRET_KEY", default="SET ME")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # set these!
    TWILIO_ACCT_SID = os.environ.get("TWILIO_ACCT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

    # dialplan
    DIALPLAN_EXT_DIAL_PREFIX = '#'  # prefix for dialing subscribers by extension

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
