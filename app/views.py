from flask import render_template
from app import app
from.request import get_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting specific source
    specific_sources=get_sources('specific')

    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title,specific= specific_sources)
