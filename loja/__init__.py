from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///minhaloja.db"
# initialize the app with the extension
app.config ['SECRET_KEY'] = 'suydgeidhoie59656'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from loja.admin import rotas