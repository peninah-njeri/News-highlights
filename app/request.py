from app import app
import urllib.request,json
from .Models import source
from .Models import article



# Getting api key
api_key = app.config['NEWS_API_KEY']