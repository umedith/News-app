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

# @app.route('/search/<movie_name>')
# def search(movie_name):    # if search_movie:
    #     return redirect(url_for('search',movie_name=search_movie))
    # else:
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)



# @app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     movie = get_movie(id)
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(movie.id,title,movie.poster,review)
#         new_review.save_review()
#         return redirect(url_for('movie',id = movie.id ))
#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)# 