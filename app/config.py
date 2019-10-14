class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources&from=2019-09-13&sortBy=publishedAt&apiKey=1621d331facd44f380fedf77cc13b2e5'

    ARTICLE_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=1621d331facd44f380fedf77cc13b2e5'

    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True