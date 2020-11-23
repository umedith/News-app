from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources
from .request import get_source_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting artcle sources
    all_sources = get_sources()
    title = 'Home - Welcome to E-News Website'

    return render_template('index.html', title = title, sources = all_sources )

@app.route('/articles/<id>')
def articles(id):
    '''
    View articles page function that returns the articles page and its data
    '''
    
    # Getting artcle sources
    all_article = get_source_articles(id)
    title = 'All articles'

    return render_template('articles.html', title = title, articles = all_article )
