import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/mypitch'
    
    SECRET_KEY = "newSecretKey@"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

   


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`



class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kibet:KibetFlask@localhost/mypitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}