from app import app
import urllib.request,json
from .models import article
from .models import source
Source = source.Source
Article = article.Article
#Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# getting sources
def get_sources():
    
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url + 'sources?apiKey='+ format(api_key)
    news_results = None
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        

        if get_news_response['status'] == 'ok':
            news_results_list = get_news_response['sources']
            news_results = process_sources_results(news_results_list)
            # print(news_results)
    
    return news_results
def get_source_articles(id):

    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = base_url + 'everything?sources='+id+'&apiKey='+ format(api_key)

    articles_results = None
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        

        if get_articles_response['status'] == 'ok':
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
            
    
    return articles_results

def process_articles_results(articles_list):

    '''
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain articles details
    Returns :
        sources_results: A list of articles objects
    '''

    articles_results = []
    for article_item in articles_list:

        id = article_item.get('id')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image_url = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        author = article_item.get('author')

        if url:
            article_object = article.Article(id,author,title,description,url,image_url,content,publishedAt)
            
            articles_results.append(article_object)
    return articles_results
def process_sources_results(source_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain sources details
    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')    
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = source.Source(id,name,description,url,category,language,country)
            
            sources_results.append(source_object)
    return sources_results
def get_news(id):
    get_news_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            # vote_count = movie_details_response.get('vote_count')
            news_object = News(id,name,descriprion,url,category,)
    return news_object
    
def search_news(_name):
    search_news_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)
        search_movie_results = None
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)
    return search_movie_results