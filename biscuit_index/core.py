from flask import (Flask, g, request, session, redirect,
        url_for, render_template, flash)
import redis
import os
from biscuit_index.biscuit_index import config as config_file

app = Flask('biscuit_index')
app.config.from_object(config_file)

def get_db():
    if not hasattr(g, 'redis'):
        g.redis = redis.StrictRedis(**app.config['REDIS'])
    return g.redis

### VIEWS

@app.route('/')
def home():
    db = get_db()
    values = db.get('nairobi')
    return "<html> <body>%s</body> </html>" % values


### END OF VIEWS
