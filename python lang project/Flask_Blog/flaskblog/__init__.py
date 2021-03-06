from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)


app.config['SECRET_KEY'] = 'b56b7ffac293280f99ea40f456641c04'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'liljearsy@gmail.com'
app.config['MAIL_PASSWORD'] = '47h_m@luaA24'
mail = Mail()

# our routes import the flask app
# so we cant import routes in this file
# before we create the app
# or else we will get a circular import error
from flaskblog import routes