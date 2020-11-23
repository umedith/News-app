import os

class Config:
    """
    General configuration parent class
    """   
    NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL = os.environ.get('NEWS_API_BASE_URL')

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
         Config: The pareny configuration class with General configuration settings
    """
    pass
class DevConfig(Config):
    """
    Dvelopment configuration child class
    Args:
         Config: The parent configuration class woth Gneral configuration settings
    """
    DEBUG = True