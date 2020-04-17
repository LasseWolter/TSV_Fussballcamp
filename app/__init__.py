from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application,db)
login = LoginManager(application)
login.login_view='login'

# polyfill for altering tables in case of SQLite
with application.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(application, db, render_as_batch=True)
    else:
        migrate.init_app(application, db)

from app import routes, models
