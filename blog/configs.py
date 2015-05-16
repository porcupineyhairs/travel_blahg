class Config(object):
  SECRET_KEY = 'G00DB33F'
  ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
  UPLOAD_FOLDER = 'uploads'

  CACHE_TYPE = 'simple'

class DevConfig(Config):
  DEBUG = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  UPLOAD_FOLDER = 'dev_uploads'

  SQLALCHEMY_DATABASE_URI = 'sqlite:///../dev_database.db'

  CACHE_TYPE = 'null'

class TestConfig(Config):
  DEBUG = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  UPLOAD_FOLDER = 'test_uploads'

  import tempfile
  db_file = tempfile.NamedTemporaryFile()
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
  SQLALCHEMY_ECHO = True

  CACHE_TYPE = 'null'
  WTF_CSRF_ENABLED = False

