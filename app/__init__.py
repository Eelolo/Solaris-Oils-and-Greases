from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    from .admin_views import admin_bp
    app.register_blueprint(admin_bp)

    from .views import main_bp
    app.register_blueprint(main_bp)

    db.init_app(app)

    app.jinja_options['extensions'].append('jinja2.ext.loopcontrols')

    return app
