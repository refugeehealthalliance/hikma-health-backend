import os
ENV = os.environ.get('APP_ENV', 'dev_local')

FLASK_DEBUG_PORT = 5000

if ENV in ('dev_local', 'dev_docker', 'stg'):
    if ENV in ('dev_local', 'stg'):
        PG_HOST = 'localhost'
    elif ENV == 'dev_docker':
        PG_HOST = 'db'

    PG_USER = 'postgres'
    # PG_PASSWORD = 'password'
    PG_PASSWORD = 'postgres'
    PG_DB = 'hikma_dev'
    FLASK_DEBUG = True
    PHOTOS_STORAGE_BUCKET = 'dev-api-photos'
    EXPORTS_STORAGE_BUCKET = 'dev-api-exports'
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = 'bd227f3d-0fbb-45c5-beed-8ce463481415'

if ENV == 'prod':
    FLASK_DEBUG = False
    PG_USER = "vkzbqvihuqwqph"
    PG_PASSWORD = "49628d30114e98fe638f00d51f04a765423712501a0ff3648d038c3973738e03"
    PG_HOST = 'ec2-3-213-228-206.compute-1.amazonaws.com'
    PG_DB = "d6n55if55sp02s"
    PHOTOS_STORAGE_BUCKET = os.environ['PHOTOS_STORAGE_BUCKET']
    EXPORTS_STORAGE_BUCKET = os.environ['EXPORTS_STORAGE_BUCKET']
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = os.environ['DEFAULT_PROVIDER_ID']