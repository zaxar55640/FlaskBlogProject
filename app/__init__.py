from flask import Flask
from extensions import db
from flask_login import LoginManager
from entities.user import User


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    db.init_app(app)
    login_manager.init_app(app)
    from models.admin import admin
    from models.main import main
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(main)
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app = create_app()
    app.run()