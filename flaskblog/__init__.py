from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f40b39db60e629dbd5f7a0194d9654ab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
ckeditor = CKEditor(app)
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# from flaskblog import routes



from flaskblog.users.routes import users
from flaskblog.main.routes import main
from flaskblog.blog.routes import posts

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)