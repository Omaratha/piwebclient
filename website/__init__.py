from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# creating database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "omkomkomkomk"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #setting up sql database path for app
    db.init_app(app) #this cmd tell database to use with this app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Serverconfig
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    from .models import Serverconfig
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
            setServerConfig = Serverconfig(nrIp='192.168.1.100', serverName='nodered', apiUrl='/sensor/triggered', payloadMsg='{"dataKay":"dataValue"}')
            db.session.add(setServerConfig)
            db.session.commit()
            print('Created Database!')
