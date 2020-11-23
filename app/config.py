 
class Config:
    """
    General configuration parent class
    """   
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
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