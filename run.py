import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import init_db


app = Flask(__name__)

# testing secret_key
SECRET_KEY = os.getenv('SECRET_KEY', 'Optional default value')
app.secret_key = SECRET_KEY

# app.config.from_pyfile('config.py')

from models import *

init_db()

# app views
from base_views import *
from reg_views import *
from profile_views import *
from edit_views import *
from del_views import *
from catch_views import *
from search_views import *


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')))

