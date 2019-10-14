from flask import render_template
from app import app
from .request import get_source
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_sources= get_source('popular')


    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title,popular= popular_sources)
