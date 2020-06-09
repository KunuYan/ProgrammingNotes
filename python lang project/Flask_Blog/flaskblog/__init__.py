from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'b56b7ffac293280f99ea40f456641c04'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# our routes import the flask app
# so we cant import routes in this file
# before we create the app
# or else we will get a circular import error
from flaskblog import routes