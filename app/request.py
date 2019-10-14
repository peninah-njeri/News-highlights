from app import app
import urllib.request,json
from .Models import source
from .Models import article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

    # Getting the source and article url base
base_url =app.config['NEWS_API_BASE_KEY']
article_url=app.config['ARTICLE_API_BASE_URL'] 


def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source in source_list:
        id = source.get('id')
        name= source.get('name')
        description= source.get('description')

        if id:
            source_object = Source(id,name,description)
            source_results.append(source_object)
        
    return source_results

    