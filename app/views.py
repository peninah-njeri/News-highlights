from flask import render_template
from app import app
from .request import get_source, get_article
# Views
@app.route('/')
def index():
    
    
    '''
    View root page function that returns the index page and its data
    '''
# Getting popular news
    general_news = get_source('general')
    entertainment_news = get_source("entertainment")
    sports_news = get_source("sports")
    print(entertainment_news)
    title = 'Home - Welcome to The best News Highlight Website Online'
    return render_template('index.html', title=title, general=general_news, entertainment=entertainment_news, sports=sports_news)


@app.route('/article/<id>')
def article(id):
    '''
    View news page function that returns the news details page and its data
    '''
    article = get_article(id)
    # title = f'{article.title}'
    return render_template('article.html', article=article)
